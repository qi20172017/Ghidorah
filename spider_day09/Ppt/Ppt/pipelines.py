# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.files import FilesPipeline
import scrapy
class PptPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        return scrapy.Request(item['ppt_file'],meta={'item':item})


    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        sort_name = item['sort_name']
        ppt_name = item['ppt_name'] + request.url[-4:]
        return '%s/%s' % (sort_name, ppt_name)
    # "http://ppt.1ppt.com/uploads/soft/2002/1-200225092010.zip"
