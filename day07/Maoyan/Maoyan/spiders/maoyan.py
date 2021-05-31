# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']

    def start_requests(self):
        url = 'https://maoyan.com/board/4?offset={}'
        for i in range(0,91,10):
            full_url = url.format(i)
            print(full_url)
            yield scrapy.Request(url=full_url,callback=self.parse)

    def parse(self, response):
        item = MaoyanItem()
        move_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        for move in move_list:
            item['name'] = move.xpath('.//p[@class="name"]/a/text()').get().strip()
            item['star'] = move.xpath('.//p[@class="star"]/text()').get().strip()
            item['time'] = move.xpath('.//p[@class="releasetime"]/text()').get().strip()
            yield item
