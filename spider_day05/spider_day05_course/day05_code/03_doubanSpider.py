"""
抓取豆瓣电影排行榜-类别(Ajax动态加载)
"""
import requests
import json
from fake_useragent import UserAgent
import time
import random

class DoubanSpider:
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start={}&limit=20'
        self.i = 0

    def get_html(self,url):
        """请求功能函数"""
        headers = { 'User-Agent':UserAgent().random }
        html = requests.get(url=url,headers=headers).text

        return html

    def parse_html(self,url):
        # html: [{},{},{},{},{}]
        html = json.loads(self.get_html(url))
        item = {}
        for one_film in html:
            item['name'] = one_film['title']
            item['time'] = one_film['release_date']
            item['score'] = one_film['score']
            print(item)
            self.i += 1

    def run(self):
        total = self.get_total()
        for start in range(0,total,20):
            url = self.url.format(start)
            self.parse_html(url)
            # 休眠
            time.sleep(random.uniform(0,1))
        print('数量:',self.i)

    def get_total(self):
        """获取电影总数函数"""
        url = 'https://movie.douban.com/j/chart/top_list_count?type=13&interval_id=100%3A90'
        html = json.loads(self.get_html(url))
        total = html['total']

        return total

if __name__ == '__main__':
    spider = DoubanSpider()
    spider.run()





















