# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymongo
from .settings import *
class TencentjobPipeline(object):
    def process_item(self, item, spider):
        print(item)
        return item

class TencentjobMysqlPipeline(object):
    def open_spider(self,spider):
        self.db = pymysql.connect(MYSQL_HOST,MYSQL_USER,MYSQL_PWD,MYSQL_DB,charset=CHARSET)
        self.cursor = self.db.cursor()

    def process_item(self,item,spider):
        data = [
            item['name'],
            item['time'],
            item['address'],
            item['sort'],
            item['resp'],
            item['require'],
        ]
        ins = 'insert into tencenttab values(%s,%s,%s,%s,%s,%s)'
        self.cursor.execute(ins,data)
        self.db.commit()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()