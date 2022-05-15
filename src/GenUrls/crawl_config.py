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


# Blacklist snippits
# can also be a path like: '/tags/'
DENY = (
	'wp-login.php',
)


# Log level to use for output while spider is activly crawling
# Available: 'CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'
LOG_LEVEL = 'ERROR'


# What format and file name to save the results in
FEED_FORMAT = 'csv'
FEED_URI = 'RESULTS.csv'


# Obey what is in robots.txt
OBEY = False