# -*- coding: utf-8 -*-
import scrapy

class FlipkartspiderSpider(scrapy.Spider):
    name = 'flipkartSpider'
    allowed_domains = ['https://www.flipkart.in/']
    start_urls = ['https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.serviceability%5B%5D%3Dfalse&otracker=categorytree&page=%s'.replace('%s',str(page)) for page in range(2,10)]
    def parse(self, response):
        name=response.xpath('//div[@class = "_3wU53n"]/text()').extract()
        price=response.xpath('//div[@class = "_1vC4OE _2rQ-NK"]/text()').extract()
        for Product_Name, Product_Price in zip(name, price):
            yield {'Product_Name': Product_Name.strip(), 'Product_Price': Product_Price.strip()}
        pass

