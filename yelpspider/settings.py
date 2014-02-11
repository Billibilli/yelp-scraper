# Scrapy settings for yelpspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'yelpspider'

SPIDER_MODULES = ['yelpspider.spiders']
NEWSPIDER_MODULE = 'yelpspider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'yelpspider (+http://www.yourdomain.com)'
