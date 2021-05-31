# -*- coding: utf-8 -*-
import scrapy


class SouSpider(scrapy.Spider):
    name = 'sou'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        result = response.xpath('//*[@id="su"]/@value')
        print('*'*60)
        print(result.extract())
        print('*'*60)
