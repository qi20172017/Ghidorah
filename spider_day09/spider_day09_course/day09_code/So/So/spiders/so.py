# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import SoItem

class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['image.so.com']
    url = 'https://image.so.com/zjl?ch=beauty&sn={}&listtype=new&temp=1'

    # 重写start_requests()方法
    def start_requests(self):
        # 拼接多页地址,交给调度器入队列
        for sn in range(0,91,30):
            page_url = self.url.format(sn)
            yield scrapy.Request(url=page_url,callback=self.parse)

    def parse(self, response):
        """提取：图片的链接"""
        html = json.loads(response.text)
        for one_img in html['list']:
            # 创建item对象
            item = SoItem()
            item['img_url'] = one_img['qhimg_url']
            item['img_title'] = one_img['title']

            # 此处不需要将图片链接交给调度器,直接交给管道即可
            # 管道文件中,scrapy已定义了图片管道类
            yield item

