import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from GenUrls.spiders.genurls_bot import GenUrlsBot
from GenUrls import crawl_config


# Consume settings and start crawl
process = CrawlerProcess(get_project_settings())
process.crawl(GenUrlsBot)
process.start()
