import requests
from fake_useragent import UserAgent
from threading import Thread,Lock
from queue import Queue
import csv

class XiaomiSpider(object):
    def __init__(self):
        self.url = 'http://app.mi.com/categotyAllListApi?page=3&categoryId=2&pageSize=30'
        self.f = open('xiaomi2.csv','a')
        self.writer = csv.writer(self.f)
        self.q = Queue()
        self.lock = Lock()

    def get_info(self,url):
        headers = {
            'User-Agent':UserAgent().random
        }
        html = requests.get(url,headers=headers)
        return html.json()['data']

    def url_in(self):
        for i in range(67):
            url = self.url.format(i)
            self.q.put(url)

    def parse_html(self):
        while True:
            self.lock.acquire()
            if not self.q.empty():
                url = self.q.get()
                self.lock.release()
                info = self.get_info(url)
                item = {}
                one_page_list = []
                for app in info:
                    item['name']=app['displayName']
                    item['type']=app['level1CategoryName']
                    item['link']=app['packageName']
                    one_page_list.append((item['name'],item['type'],item['link']))
                self.lock.acquire()
                self.writer.writerows(one_page_list)
                self.lock.release()
            else:
                self.lock.release()
                break

    def run(self):
        self.url_in()
        t_list = []
        for i in range(5):
            t = Thread(target=self.parse_html)
            t_list.append(t)
            t.start()
        for t in t_list:
            t.join()



if __name__ == '__main__':
    myspider = XiaomiSpider()
    myspider.run()