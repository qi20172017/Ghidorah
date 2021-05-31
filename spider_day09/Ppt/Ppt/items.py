# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PptItem(scrapy.Item):
    # define the fields for your item here like:
    sort_name = scrapy.Field()
    sort_link = scrapy.Field()
    ppt_name = scrapy.Field()
    ppt_link = scrapy.Field()
    ppt_file = scrapy.Field()
