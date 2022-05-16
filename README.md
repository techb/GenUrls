# GenUrls
A python tool to crawl a website for all _linked_ urls, similar to [ScreamingFrog](https://www.screamingfrog.co.uk/seo-spider/) but without the ~~bloat~~ features.

Will crawl the website and follow links found within the HTML. There is a config file to set domains, robot.txt obey, black listed urls/snippits, and output file.

There is no guarentee to find all pages/posts/urls on a website, if the page is not linked anywhere on the website, this bot will not find it (targeted marketing landing pages for example).

No recurrsion limits and `CONCURRENT_REQUESTS` set to 32 by default.

## Requirements
---
- Python3
- venv :: `sudo apt install python3.8-venv`
- [Scrapy](https://scrapy.org/) (handled in requirements.txt)


## Install
---
**Windows users are assumed to be in WSL**
- `$ git clone git@github.com:techb/GenUrls.git`
- `$ cd GenUrls`
- `$ python3 -m venv venv`
- `$ source venv/bin/activate`
- `(venv)$ pip install -r requirements.txt`


## Settings
---
- **`./scr/GenUrls/crawl_config.py`**
  - **DOMAINS** :: allowed domains to crawl
  - **ENTRYURLS** :: url where the spider starts.
    - sitemap and/or homepage is a good starting point
  - **DENY** :: strings,urls,paths to blacklist
  - **LOG_LEVEL** :: level of output in terminal when activly crawling
  - **FEED_FORMAT** :: results file format `csv`, `json`
  - **FEED_URI** :: path and file name of the results, defaults to same dir with `RESULTS` as name
  - **OBEY** :: obey the robots.txt file, `False` will ignore it, `True` will obey


## Run
---
- `(venv)$ cd src`
- `(venv)$ python run_spider.py`


## Dev
---
Besides config, most dev happens in `./src/GenUrls/spiders/genurls_bot.py`.

### GenUrlsBot
Driving class of the crawling spider.
#### Properties
- **name** :: Spiders name
- **allowed_domains** :: List of domains that the spider can crawl.
  - `./src/GenUrls/crawl_config.py` :: **DOMAINS**
- **start_urls** :: List of entry point urls to start the crawl.
  - `./src/GenUrls/crawl_config.py` :: **ENTRYURLS**
- **handle_httpstatus_list** :: List of HTTP status codes to watch for.
- **crawled_data** :: List of Dict's holding all crawled urls and class data.
- **rules** :: List of Scrapy Rules containing a LinkExtractor,  callback, follow, and deny.
