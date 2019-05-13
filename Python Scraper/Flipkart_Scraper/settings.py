# -*- coding: utf-8 -*-

# Scrapy settings for flip project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Flipkart_Scraper'

SPIDER_MODULES = ['Flipkart_Scraper.Flipkart_Scraper.spiders']
NEWSPIDER_MODULE = 'Flipkart_Scraper.Flipkart_Scraper.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
FEED_URI = 'data/%(name)s/%(time)s_output.csv'
FEED_FORMAT = 'csv'
