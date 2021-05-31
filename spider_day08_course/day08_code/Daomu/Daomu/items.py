# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DaomuItem(scrapy.Item):
    # define the fields for your item here like:
    pian_name = scrapy.Field()
    pian_link = scrapy.Field()
    zang_name = scrapy.Field()
    zang_link = scrapy.Field()
    duan_name = scrapy.Field()
    duan_content = scrapy.Field()
    file_path = scrapy.Field()

