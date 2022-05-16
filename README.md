# GenUrls
A python tool to crawl a website for all _linked_ urls, similar to [ScreamingFrog](https://www.screamingfrog.co.uk/seo-spider/) but without the bloat.

Will crawl the website and follow links found with-in the HTML. There is a config file to set domains, robot.txt obey, black listed urls, etc...

There is no guarentee to find all pages/posts/urls on a website, if the page is not linked anywhere on the website, this bot will not find it (targeted marketing landing pages for example).

If on Windows, it is assumed you are inside WSL.


Spider based on [Scrapy's](https://scrapy.org/) 
- [CrawlSpider class](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.CrawlSpider)

## Requirements
---
- Python3
- venv


## Install
---
- `$ git clone this-repo`
- `$ python3 -m venv venv`
- `$ source venv/bin/active`
- `$ pip install -r requirements.txt`


## Settings
---
- **`./scr/GenUrls/crawl_config.py`**
  - **DOMAINS** :: allowed domains to crawl
  - **ENTRYURLS** :: url where the spider starts
  - **DENY** :: strings/urls/paths to blacklist
  - **LOG_LEVEL** :: level of output in terminal when activly crawling
  - **FEED_FORMAT** :: results file format `csv`, `json`
  - **FEED_URI** :: path and file name of the results, defaults to same dir with `RESULTS` as name
  - **OBEY** :: obey the robots.txt file, `False` will ignore it, `True` will obey


## Run
- `(venv)$ cd src`
- `(venv)$ python run_spider.py`
