yelp-scraper
============

scrape information about business from yelp search page

Prerequisite: scrapy

Installation in Debian:

sudo apt-get install python-pip

pip install scrapy


Run:

scrapy crawl yelp -o scraped_yelp.json -t json
