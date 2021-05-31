"""
小米应用商店 - 聊天社交应用 - 多线程抓取
"""
import requests
import json
from threading import Thread,Lock
import time
from fake_useragent import UserAgent
import csv
from queue import Queue

class XiaomiSpider:
    def __init__(self):
        self.url = 'http://app.mi.com/categotyAllListApi?page={}&categoryId=2&pageSize=30'
        self.i = 0
        # 存入csv文件相关变量
        # windows中存入csv,添加: newline=''参数,否则会多出空行
        self.f = open('xiaomi.csv','a',encoding='utf-8',newline='')
        self.writer = csv.writer(self.f)
        # URL队列
        self.q = Queue()
        # 锁
        self.lock = Lock()

    def get_html(self,url):
        """获取响应内容的功能函数"""
        headers = { 'User-Agent':UserAgent().random }
        html = requests.get(url=url,headers=headers).text
        return html

    def url_in(self):
        """URL地址入队列"""
        for page in range(67):
            page_url = self.url.format(page)
            self.q.put(page_url)

    def parse_html(self):
        """线程事件函数: get()地址,请求+解析+数据处理"""
        while True:
            # 加锁 - 防止出现死锁(self.q中剩余1个地址,但是被多个线程判断不为空的情况)
            self.lock.acquire()
            if not self.q.empty():
                url = self.q.get()
                self.lock.release()
                # 请求 + 解析
                try:
                    html = json.loads(self.get_html(url=url))
                    one_page_list = []
                    item = {}
                    for app in html['data']:
                        item['name'] = app['displayName']
                        item['type'] = app['level1CategoryName']
                        item['link'] = app['packageName']
                        one_page_list.append((item['name'],item['type'],item['link']))
                        print(item)
                    # 加锁和释放锁
                    self.lock.acquire()
                    self.writer.writerows(one_page_list)
                    self.lock.release()
                except Exception as e:
                    print(e)
            else:
                # 当队列为空了,释放锁(因为上面已经上锁了)
                self.lock.release()
                break

    def run(self):
        """程序的入口函数"""
        self.url_in()
        t_list = []
        for i in range(1):
            t = Thread(target=self.parse_html)
            t_list.append(t)
            t.start()

        for th in t_list:
            th.join()

if __name__ == '__main__':
    start_time = time.time()
    spider = XiaomiSpider()
    spider.run()
    end_time = time.time()
    print('时间:%.2f' % (end_time-start_time))






