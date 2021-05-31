# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentjobItem(scrapy.Item):
    # define the fields for your item here like:
    # 名称，地址，类别，时间，职责，要求
    name = scrapy.Field()
    address = scrapy.Field()
    sort = scrapy.Field()
    time = scrapy.Field()
    resp = scrapy.Field()
    require = scrapy.Field()


