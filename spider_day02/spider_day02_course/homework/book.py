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
        self.url = 'http://book.zongheng.com/store/c0/c0/b0/u0/p{}/v9/s9/t0/u0/i1/ALL.html'
        # self.url = 'https://www.4567tv.tv/index.php/vod/show/id/5/page/4.html'
        self.header = {'User-Agent':UserAgent().random}
        self.one_regex = '<div class="bookbox fl">.*?<a href="(.*?)" target="_blank">.*?</div>'
        self.two_regex = '<a class="all-catalog".*?href="(.*?)" data-sa-d='
        self.three_regex = '<li class=" col-4">.*?<a  href="(.*?)" target.*?</li>'
        self.four_regex1 = '<div class="content" itemprop="acticleBody">.*?</div>'
        self.four_regex2 = '<p>(.*?)</p>'


    def get_html(self,url):
        req = request.Request(url=url,headers=self.header)
        res = request.urlopen(req,timeout=40)
        html = res.read().decode('utf-8','ignore')
        print('访问：',res.geturl())
        return html

    def get_info(self,regex,html):
        pattern = re.compile(regex,re.S)
        return pattern.findall(html)

    def save_html(self,html):
        with open('book.html','w')as f:
            f.write(html)

    def save_info(self,info):
        sql = 'insert into movie_info values (%s,%s)'
        self.cursor.execute(info[0])
        self.db.commit()

    def run(self):
        for page in range(1,100):
            one_url = self.url.format(page)
            one_html = self.get_html(one_url)
            # self.save_html(one_html)
            one_info = self.get_info(self.one_regex,one_html)
            print(one_info)
            for info in one_info:
                time.sleep(random.uniform(1,3))
                two_html = self.get_html(info)
                two_info = self.get_info(self.two_regex,two_html)
                print(two_info)
                three_url = two_info[0]
                three_html = self.get_html(three_url)
                three_info = self.get_info(self.three_regex,three_html)
                # self.save_html(three_html)
                for url in three_info:
                    four_html = self.get_html(url)
                    # self.save_html(four_html)
                    four_info1 = self.get_info(self.four_regex1,four_html)
                    four_info2 = self.get_info(self.four_regex2,four_info1[0])
                    for i in four_info2:
                        print(i)



if __name__ == '__main__':
    myspider = MovieSpider()
    myspider.run()