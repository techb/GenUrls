import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class GenUrlsBot(CrawlSpider):
    name = 'genurls'
    allowed_domains = []
    start_urls = []
    crawled_data = []

    # Empty LinkExtractor because we want all of them.
    rules = (
        Rule(LinkExtractor(deny=('wp-login.php')), callback='parse_item', follow=True),
    )


    def __init__(self, domains=[], starturls=[]):
        super(GenUrlsBot, self).__init__(domains=[], starturls=[])
        self.allowed_domains = domains
        self.start_urls = starturls


    def parse_item(self, response):
        item = {
            'start_url': response.request.url,
            'url': response.url,
            'status': response.status
        }
        self.crawled_data.append(item)
        print(item)

        return item

