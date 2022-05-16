import json
import csv
from pprint import pprint
from urllib.request import urljoin
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from .. import crawl_config
from scrapy.utils.python import to_native_str


class GenUrlsBot(CrawlSpider):
    name = 'genurls'
    allowed_domains = crawl_config.DOMAINS
    start_urls = crawl_config.ENTRYURLS
    handle_httpstatus_list = [301, 302, 404, 200]
    crawled_data = []
    redirects_found = 0
    notfound_links = 0

    # Only specifying the deny since we want ALL urls minus a blacklist
    rules = [
        Rule(
            LinkExtractor(deny=crawl_config.DENY),
            callback='parse_item',
            follow=True
        ),
    ]


    def _debug(self, x):
        '''
        Pretty debug in the terminal
        '''
        print('-'*15)
        pprint(x)
        print('-'*15)


    def closed(self, reason):
        '''
        Method that is ran when the spider exits.
        Save to disk the urls the spider found so far.
        Config in ./src/GenUrls/crawl_config.py
            FEED_FORMAT :: csv or json
            FEED_URI :: absolute path of where the file is written
        '''
        if crawl_config.FEED_FORMAT == 'json':
            with open(crawl_config.FEED_URI, 'w') as output:
                output.write(json.dumps(self.crawled_data))
        else:
            csv_columns = self.crawled_data[0].keys()
            with open(crawl_config.FEED_URI, 'w', newline='') as output:
                csvout = csv.DictWriter(output, csv_columns)
                csvout.writeheader()
                csvout.writerows(self.crawled_data)
        print(f"------------ {reason} ------------")
        print(f"URLs crawled: {len(self.crawled_data)}")
        print(f"404's found: { self.notfound_links}")
        print(f"301's found: { self.redirects_found}")
        print('------------------------------------')


    def handle_redirects(self, res):
        '''
        Handles 301 - 307 redirects.
        Returns the destination url of the redirect.
        Yoink: https://stackoverflow.com/a/39788550/5182044
        '''
        # HTTP header is ascii or latin1, redirected url will be percent-encoded utf-8
        location = to_native_str(
            res.headers['location'].decode('latin1'))

        # get the original request
        request = res.request
        # and the URL we got redirected to
        redirected_url = urljoin(request.url, location)

        if res.status in (301, 307) or request.method == 'HEAD':
            redirected = request.replace(url=redirected_url)
        else:
            redirected = request.replace(
                url=redirected_url, method='GET', body='')
            redirected.headers.pop('Content-Type', None)
            redirected.headers.pop('Content-Length', None)

        return redirected.url


    def parse_item(self, response):
        '''
        Callback method with a successful or redirected page hit.
        Adds found urls to self.crawled_data to be written to disk on exit.
        '''
        # if no redirects, then this remains None
        redir_url = None

        if response.status >= 300 and response.status < 400:
            redir_url = self.handle_redirects(response)
            self.redirects_found += 1
        elif response.status >= 400 and response.status < 500:
            self.notfound_links += 1

        # A new row in the generated json/csv
        item = {
            'start_url': response.url,
            'redirected': redir_url,
            'status': response.status
        }

        self.crawled_data.append(item)
        self._debug(item)

        yield item
