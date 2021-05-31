# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from .settings import *
import pymongo
class GuaziPipeline(object):
    def process_item(self, item, spider):
        print(item['name'],item['name'],item['url'])
        return item

class GuaziMysqlPipeline(object):
    def open_spider(self,spider):
        self.db = pymysql.connect(MYSQL_HOST,MYSQL_SUER,MYSQL_PWD,MYSQL_DB,charset=MYSQL_CHARSET)
        self.cursor = self.db.cursor()

    def process_item(self,item,spider):
        ins = 'insert into guaziset values(%s,%s,%s)'
        car_li = [item['name'],item['name'],item['url']]
        self.cursor.execute(ins,car_li)
        self.db.commit()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()

class GuaziMongoPipeline(object):
    def open_spider(self,spider):
        self.conn = pymongo.MongoClient(host=MONGO_HOST,port=MONGO_PORT)
        self.db = self.conn[MONGO_DB]
        self.set = self.db[MONGO_SET]
    def process_item(self,item,spider):
        data = {
            'name':item['name'],
            'price':item['price'],
            'url':item['url']}
        self.set.insert_one(data)
        return item
    # def close_spider(self,spider):
    #     pass