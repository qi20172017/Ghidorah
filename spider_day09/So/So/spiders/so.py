# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import SoItem
class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['image.so.com']
    url = 'https://image.so.com/zjl?ch=beauty&sn={}&listtype=new&temp=1'
    def start_requests(self):
        for page in range(0,61,30):
            page_url = self.url.format(page)
            yield scrapy.Request(url=page_url,callback=self.parse)

    def parse(self, response):

        data = json.loads(response.text)
        for link in data['list']:
            item = SoItem()
            item['img_url']=link['qhimg_url']
            item['img_title'] = link['title']
            yield item
