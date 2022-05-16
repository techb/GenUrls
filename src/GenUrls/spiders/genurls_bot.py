from six.moves.urllib.parse import urljoin
import scrapy
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


    # Empty LinkExtractor because we want all of them.
    rules = (
        Rule(
            LinkExtractor(deny=crawl_config.DENY),
            callback='parse_item',
            follow=True
        ),
    )


    def parse_item(self, response):
        start_url =  response.request.url
        redir_url =  None

        # Yoink: https://stackoverflow.com/a/39788550/5182044
        # handle redirection
        # this is copied/adapted from RedirectMiddleware
        if response.status >= 300 and response.status < 400:

            # HTTP header is ascii or latin1, redirected url will be percent-encoded utf-8
            location = to_native_str(response.headers['location'].decode('latin1'))

            # get the original request
            request = response.request
            # and the URL we got redirected to
            redirected_url = urljoin(request.url, location)

            if response.status in (301, 307) or request.method == 'HEAD':
                redirected = request.replace(url=redirected_url)
            else:
                redirected = request.replace(url=redirected_url, method='GET', body='')
                redirected.headers.pop('Content-Type', None)
                redirected.headers.pop('Content-Length', None)

            redir_url = redirected.url

        item = {
            'start_url': response.url,
            'redirected': redir_url,
            'status': response.status
        }

        self.crawled_data.append(item)
        print(item)
        yield item
