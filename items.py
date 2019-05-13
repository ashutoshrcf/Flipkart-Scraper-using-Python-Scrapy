# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FlipItem(scrapy.Item):
    prod_name=scrapy.Field()
    prod_price=scrapy.Field()
    pass
