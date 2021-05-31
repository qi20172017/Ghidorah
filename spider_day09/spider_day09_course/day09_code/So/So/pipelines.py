# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# scrapy提供的图片管道的类
from scrapy.pipelines.images import ImagesPipeline
# 文件管道类
from scrapy.pipelines.images import FilesPipeline
from scrapy.pipelines.media import MediaPipeline
import scrapy

class SoPipeline(ImagesPipeline):
    # 重写get_media_requests()方法,把图片链接交给调度器入队列
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['img_url'],meta={'item':item})

    # 重写file_path()方法,处理文件名的问题
    def file_path(self, request, response=None, info=None):
        # 请求对象request中,所有的属性为 Request() 中的参数
        # 比如: request.url  request.meta ... ...
        title = request.meta['item']['img_title']
        # 把title中不能作为文件名的特殊字符处理一遍,因为Windows中的文件名中不能包含这些
        all_chars = '\/*?:<>"|'
        for char in title:
            if char in all_chars:
                title = title.replace(char,'')

        filename = title + '.' + request.url.split('.')[-1]

        return filename




