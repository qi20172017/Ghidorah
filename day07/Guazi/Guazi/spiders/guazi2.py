# -*- coding: utf-8 -*-
import scrapy
from ..items import GuaziItem

class GuaziSpider(scrapy.Spider):
    name = 'guazi2'
    allowed_domains = ['www.guazi.com']
    # start_urls = ['https://www.guazi.com/jn/buy/o1/#bread']

    # 重够该方法
    def start_requests(self):
        for i in range(1,6):
            url = "https://www.guazi.com/jn/buy/o{}/#bread".format(i)
            yield scrapy.Request(url=url,callback=self.parse)

# https://www.guazi.com/jn/buy/o4/#bread
    def parse(self, response):

        li_list = response.xpath('//ul[@class="carlist clearfix js-top"]/li')
        # print(response.text)
        item = GuaziItem()
        for li in li_list:
            item['url'] = li.xpath('./a[1]/@href').extract()[0]
            item['name'] = li.xpath('.//h2[@class="t"]/text()').extract()[0]
            item['price'] = li.xpath('.//div[@class="t-price"]/p/text()').extract()[0]
            yield item
