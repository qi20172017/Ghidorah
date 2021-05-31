# -*- coding: utf-8 -*-
import scrapy


class Mysp01Spider(scrapy.Spider):
    name = 'mysp01'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        result = response.xpath('//*[@id="su"]/@value').extract()
        print('*'*60)
        print(result)
        print('*'*60)

