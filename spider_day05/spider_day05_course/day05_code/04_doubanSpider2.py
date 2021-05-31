"""
抓取豆瓣电影排行榜-类别(Ajax动态加载)
全站抓取
"""
import requests
import json
from fake_useragent import UserAgent
import time
import random
import re
import pymongo

class DoubanSpider:
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90&action=&start={}&limit=20'
        self.i = 0
        # 存入mongodb
        self.conn = pymongo.MongoClient('localhost',27017)
        self.db = self.conn['doubandb']
        self.myset = self.db['doubanset']

    def get_html(self,url):
        """请求功能函数"""
        headers = { 'User-Agent':UserAgent().random }
        html = requests.get(url=url,headers=headers).text

        return html

    def parse_html(self,url):
        # html: [{},{},{},{},{}]
        html = json.loads(self.get_html(url))

        for one_film in html:
            # 存入mongodb: item必须在for循环内
            item = {}
            item['name'] = one_film['title']
            item['time'] = one_film['release_date']
            item['score'] = one_film['score']
            print(item)
            self.i += 1
            # 存入Mongodb
            self.myset.insert_one(item)

    def run(self):
        # all_dict: {'剧情':'11','喜剧':'5','爱情':'13'}
        all_dict = self.get_all_type()
        menu = ''
        for one in all_dict:
            menu = menu + one + '|'
        print(menu)
        c = input('请输入你的选择:')
        # 获取用户输入的类别码
        typ = all_dict[c]
        total = self.get_total(typ)
        for start in range(0,total,20):
            url = self.url.format(typ,start)
            self.parse_html(url)
            # 休眠
            time.sleep(random.uniform(0,1))
        print('数量:',self.i)

    def get_total(self,typ):
        """获取电影总数函数"""
        url = 'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90'.format(typ)
        html = json.loads(self.get_html(url))
        total = html['total']

        return total

    def get_all_type(self):
        """获取所有类别的电影类别及type的值"""
        url = 'https://movie.douban.com/chart'
        html = self.get_html(url)
        regex = '<a href=".*?type_name=(.*?)&type=(.*?)&interval_id=100:90&action=">'
        pattern = re.compile(regex,re.S)
        # r_list: [('剧情','11'),('喜剧','5'),(),()]
        r_list = pattern.findall(html)
        all_dict = {}
        for r in r_list:
            all_dict[r[0]] = r[1]

        return all_dict

if __name__ == '__main__':
    spider = DoubanSpider()
    spider.run()





















