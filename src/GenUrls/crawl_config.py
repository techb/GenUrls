from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

# Allowed domains
# Usually just the domain we're scraping
#   to avoid crawling off-site links
DOMAINS = [
	'dev.kbcarte.com'
]


# Urls where the spider should start
# A sitemap might be better served here
ENTRYURLS = [
	'https://dev.kbcarte.com'
]


# Blacklist snippits using regex
DENY = [
	r'wp-login\.php',
]


# Log level to use for output while spider is activly crawling
# Available: 'CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'
LOG_LEVEL = 'ERROR'


# What format and file name to save the results in
FEED_FORMAT = 'csv'
FEED_URI = 'RESULTS.csv'


# Obey what is in robots.txt
OBEY = False


# Empty LinkExtractor because we want all of them.
# rules = (
# 	Rule(
# 		LinkExtractor(deny=crawl_config.DENY),
# 		callback='parse_item',
# 		follow=True
# 	),
# )

# def build_allowed():
# 	rule_instances = []
# 	for i in ALLOW:
# 		rule_instances.append(
# 			Rule(
# 				LinkExtractor(deny=DENY, allow=i),
# 				callback='parse_item',
# 				follow=True
# 			)
# 		)
# 	print( tuple(rule_instances) )
# 	return tuple(rule_instances)