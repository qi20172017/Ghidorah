import pymysql
from urllib import request,parse
from hashlib import md5
import time
import random
import re
from fake_useragent import UserAgent

class MovieSpider():
    def __init__(self):
        self.db = pymysql.connect('localhost','root','123456','maoyandb',charset='utf8')
        self.cursor = self.db.cursor()
        self.url = 'https://www.4567tv.tv/index.php/vod/show/id/5/page/{}.html'
        # self.url = 'https://www.4567tv.tv/index.php/vod/show/id/5/page/4.html'
        self.header = {'User-Agent':UserAgent().random}
        self.one_regex = '<li class="col-md-6 col-sm-4 col-xs-3">.*?href="(.*?)" title'
        self.two_regex = '<h1 class="title">(.*?)</h1>.*?<span class="detail-sketch">(.*?)</span>'

    def get_html(self,url):
        req = request.Request(url=url,headers=self.header)
        res = request.urlopen(req,timeout=40)
        html = res.read().decode()
        return html

    def get_info(self,regex,html):
        pattern = re.compile(regex,re.S)
        return pattern.findall(html)

    def save_html(self,html):
        with open('4567.html','w')as f:
            f.write(html)

    def save_info(self,info):
        sql = 'insert into movie_info values (%s,%s)'
        self.cursor.execute(info[0])
        self.db.commit()

    def run(self):
        one_url = self.url.format(3)
        one_html = self.get_html(one_url)
        # self.save_html(one_html)
        one_info = self.get_info(self.one_regex,one_html)
        print(one_info)
        for info in one_info:
            time.sleep(random.uniform(3,5))
            two_url = 'https://www.4567tv.tv' + info

            two_html = self.get_html(two_url)
            two_info = self.get_info(self.two_regex,two_html)
            print(two_info)

if __name__ == '__main__':
    myspider = MovieSpider()
    myspider.run()