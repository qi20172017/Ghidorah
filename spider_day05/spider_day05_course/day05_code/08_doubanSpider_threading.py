"""
多线程抓取豆瓣电影
"""
import requests
import json
from queue import Queue
from threading import Thread
from fake_useragent import UserAgent
import time

class DoubanSpider:
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start={}&limit=20'
        self.q = Queue()

    def get_html(self,url):
        """请求功能函数"""
        headers = { 'User-Agent':UserAgent().random }
        html = requests.get(url=url,headers=headers).text

        return html

    def url_in(self):
        """让url地址入队列"""
        for start in range(0,376,20):
            url = self.url.format(start)
            self.q.put(url)

    def parse_html(self):
        """线程事件函数: 请求+解析+数据处理"""
        while not self.q.empty():
            url = self.q.get()
            html = json.loads(self.get_html(url))
            for one_film in html:
                # 存入mongodb: item必须在for循环内
                item = {}
                item['name'] = one_film['title']
                item['time'] = one_film['release_date']
                item['score'] = one_film['score']
                print(item)

    def run(self):
        """程序入口函数"""
        self.url_in()
        t_list = []
        for i in range(5):
            t = Thread(target=self.parse_html)
            t_list.append(t)
            t.start()

        for m in t_list:
            m.join()

if __name__ == '__main__':
    start_time = time.time()
    spider = DoubanSpider()
    spider.run()
    end_time = time.time()
    print('执行时间:%.2f' % (end_time-start_time))

























