# -*- coding: utf-8 -*-
import scrapy
from ..items import DaomuItem

class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    def parse(self, response):
        items = []
        pian_list = response.xpath('//li[contains(@id,"menu-item-20")]/a')
        for pian in pian_list:
            item = DaomuItem()
            item['pian_name'] = pian.xpath('./text()').get()
            item['pian_link'] = pian.xpath('./@href').get()
            items.append(item)
        for item in items:
            yield scrapy.Request(url=item['pian_link'],meta={'meta_1':item},callback=self.zang_parse)
    def zang_parse(self,response):
        item_1 = response.meta['meta_1']

        zang_list = response.xpath('//article')
        for zang in zang_list:
            item = DaomuItem()
            item['pian_name'] = item_1['pian_name']
            item['pian_link'] = item_1['pian_link']
            item['zang_name'] = zang.xpath('./a/text()').get()
            item['zang_link'] = zang.xpath('./a/@href').get()
            yield scrapy.Request(url=item['zang_link'],meta={'meta_2':item},callback=self.duan_parse)


    def duan_parse(self,response):
        item = response.meta['meta_2']
        article_list = response.xpath('//article[@class="article-content"]/p/text()').extract()
        item['duan_content'] = '\n'.join(article_list)
        yield item
