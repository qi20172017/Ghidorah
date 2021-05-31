# -*- coding: utf-8 -*-
import scrapy
from ..items import BaiduItem

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        item = BaiduItem()
        item['title'] = response.xpath('/html/head/title/text()').get()
        print('parse : 看不见你的笑我怎么睡得着')

        yield item
