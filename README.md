# GenUrls
A python tool to crawl a website for all linked urls.

If on Windows, it is assumed you are inside WSL.


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
- **`./scr/run_spider.py`** :: The entry point to the crawler has two lists that are passed as named arguments. Note that the `starturls` list has the http/s and the `domains` does not.
  - `domains=['exampledomain.com'],`
  - `starturls=['https://exampledomain.com'],`

- **`./src/GenUrls/settings.py`** :: Scrapy settings for the crawler.
  - `FEED_FORMAT` :: Format to save the crawled info to.
    - `csv`
    - `json` - Default
  - `FEED_URI` :: Path and filename to save the crawled info.
  - `LOG_LEVEL` :: Log level of information that is outputted to the console when ran.
    - `CRITICAL`
    - `ERROR` - Default
    - `WARNING`
    - `INFO`
    - `DEBUG`


## Run
- `(venv)$ cd src`
- `(venv)$ python run_spider.py`
