# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import hashlib
from scrapy.utils.python import to_bytes

from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.media import MediaPipeline


class SoPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return scrapy.Request(url=item['img_url'],meta={'item':item})

    def file_path(self, request, response=None, info=None):
        image_guid = request.meta['item']['img_title']
        # image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        file_name = image_guid+'.'+request.url.split('.')[-1]
        return file_name
