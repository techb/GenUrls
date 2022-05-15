from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from GenUrls.spiders.genurls_bot import GenUrlsBot


process = CrawlerProcess(get_project_settings())
process.crawl(GenUrlsBot, 
	domains=['dev.kbcarte.com'],
	starturls = ['https://dev.kbcarte.com'],
)
process.start()