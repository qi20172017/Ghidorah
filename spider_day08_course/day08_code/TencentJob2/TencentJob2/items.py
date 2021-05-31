# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Tencentjob2Item(scrapy.Item):
    # define the fields for your item here like:
    job_name = scrapy.Field()
    job_type = scrapy.Field()
    job_duty = scrapy.Field()
    job_require = scrapy.Field()
    job_address = scrapy.Field()
    job_time = scrapy.Field()
    # 具体职位链接
    job_url = scrapy.Field()
    post_id = scrapy.Field()

