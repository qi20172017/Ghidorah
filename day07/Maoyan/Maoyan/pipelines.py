# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import pymysql
from .settings import *
class MaoyanPipeline(object):
    def process_item(self, item, spider):
        print(item['name'],item['star'],item['time'])
        return item

class MaoyanMysqlPipeline(object):
    def open_spider(self,spider):
        self.db = pymysql.connect(MYSQL_HOST,MYSQL_USER,MYSQL_PWD,MYSQL_DB,charset=CHARSET)
        self.cursor = self.db.cursor()
    def process_item(self,item,spider):
        ins = "insert into maoyantab values(%s,%s,%s)"
        data = [item['name'],item['star'],item['time']]
        self.cursor.execute(ins,data)
        self.db.commit()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()