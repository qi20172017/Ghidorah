# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SinaPipeline(object):
    def process_item(self, item, spider):
        # url: http://dl.sina.com.cn/zt/auto/sinadlcyh/index.shtml
        # 文件名使用url地址的中间(即去掉协议和后缀.shtml)
        filename = item['news_url'][7:-6].replace('/','-')
        filename_ = item['son_directory'] + filename + '.txt'
        # 写入本地文件
        with open(filename_,'w',encoding='utf-8') as f:
            f.write(item['news_content'])

        return item
