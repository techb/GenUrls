# Allowed domains
# Usually just the domain we're scraping
#   to avoid crawling off-site links
DOMAINS = [
    'kbcarte.com',
    'dev.kbcarte.com'
]


# Urls where the spider should start
# A sitemap might be better served here
ENTRYURLS = [
    'https://kbcarte.com',
    'https://dev.kbcarte.com'
]


# Blacklist using regex
DENY = [
    r'wp-login\.php',
    r'tel:',
    r'mailto:',
]


# Log level to use for output while spider is activly crawling
# Available: 'CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'
LOG_LEVEL = 'ERROR'


# What format and file name to save the results in
# csv and json available
FEED_FORMAT = 'json'
FEED_URI = 'RESULTS.json'


# Obey what is in robots.txt
OBEY = False
