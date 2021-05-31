# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

class DaomuPipeline(object):
    def process_item(self, item, spider):
        print('{}: {}'.format(item['pian_name'],item['zang_name']))
        return item

class DaomuSavePipeline(object):
    def process_item(self,item,spider):
        file_dir = './novel2/{}'.format(item['pian_name'])
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        file_path = file_dir+'/{}.txt'.format(item['zang_name'])
        with open(file_path,'w')as f:
            f.write(item['duan_content'])

        return item


