# -*- coding: utf-8 -*-
import scrapy
from ..items import DaomuItem

class DaomuSpider(scrapy.Spider):
    name = 'daomu2'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    def parse(self, response):
        items = []
        pian_list = response.xpath('//li[contains(@id,"menu-item-20")]/a')
        for pian in pian_list:
            item = DaomuItem()
            pian_name = pian.xpath('./text()').get()
            item['pian_link'] = pian.xpath('./@href').get()
            items.append(item)
        for item in items:
            yield scrapy.Request(url=item['pian_link'],meta={'pian_name':pian_name},callback=self.zang_parse)

    def zang_parse(self,response):
        pian_name = response.meta['pian_name']

        zang_list = response.xpath('//article')
        for zang in zang_list:
            item = DaomuItem()
            item['pian_name'] = pian_name
            # item['pian_link'] = item_1['pian_link']
            item['zang_name'] = zang.xpath('./a/text()').get()
            zang_link = zang.xpath('./a/@href').get()
            yield scrapy.Request(url=zang_link,meta={'meta_2':item},callback=self.duan_parse)


    def duan_parse(self,response):
        item = response.meta['meta_2']
        article_list = response.xpath('//article[@class="article-content"]/p/text()').extract()
        item['duan_content'] = '\n'.join(article_list)
        yield item
