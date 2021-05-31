# -*- coding: utf-8 -*-
import scrapy
from ..items import PptItem

class PptSpider(scrapy.Spider):
    name = 'ppt'
    allowed_domains = ['www.1ppt.com']
    start_urls = ['http://www.1ppt.com/xiazai/']

    def parse(self, response):
        # html = response.text
        sort_list = response.xpath('.//div[@class="col_nav clearfix"]/ul/li[position()>1]')
        # print(response.text)
        for sort in sort_list:
            item = PptItem()
            item['sort_name'] = sort.xpath('./a/text()').get()
            item['sort_link'] = response.urljoin(sort.xpath('./a/@href').get())
            yield scrapy.Request(url=item['sort_link'],meta={'item1':item},callback=self.parse_ppt)

    def parse_ppt(self,response):
        # html = response.text
        item1 = response.meta['item1']

        if response.xpath(".//ul[@class='pages']/li[last()-1]/a/text()"):
            item = PptItem()
            item['sort_name'] = item1['sort_name']
            item['sort_link'] = item1['sort_link']
            next_page = response.urljoin(response.xpath(".//ul[@class='pages']/li[last()-1]/a/@href").get())
            yield scrapy.Request(url=next_page,meta={'item1':item},callback=self.parse_ppt)


        ppt_list = response.xpath(".//ul[@class='tplist']/li")
        for ppt in ppt_list:
            item = PptItem()
            item['sort_name'] = item1['sort_name']
            item['sort_link'] = item1['sort_link']
            item['ppt_name'] = ppt.xpath('./a/img/@alt').get()
            item['ppt_link'] = response.urljoin(ppt.xpath('./a/@href').get())
            yield scrapy.Request(url=item['ppt_link'],meta={'item2':item},callback=self.parse_conten)

    def parse_conten(self,response):
        # html = response.text
        item = response.meta['item2']
        item["ppt_file"] = response.xpath(".//ul[@class='downurllist']/li/a/@href").get()
        yield item
