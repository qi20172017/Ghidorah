import random
import re
from hashlib import md5
import pymysql
from urllib import request,parse
import time
import redis
import sys


class MoveSpider():
    def __init__(self):
        self.db = pymysql.connect('localhost','root','123456','maoyandb',charset='utf8')
        self.cursor = self.db.cursor()
        self.r = redis.Redis()
        self.url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
        self.header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0'}
        self.regix1 = '<table.*?class="tbspan".*?<a href="(.*?)".*?</table>'
        self.regix2 = '译　　名\s*(.*?)\s*<br.*<table.*?<a href="(.*?)">ftp.*?</table>'

    def get_html(self,url):
        req = request.Request(url=url,headers=self.header)
        res = request.urlopen(req,timeout=8)
        html = res.read().decode('gb2312','ignore')
        # print(html)
        return html

    def get_info(self,regix,html):
        pattern = re.compile(regix, re.S)
        return pattern.findall(html)

    def save_html(self,html):
        with open('second.html','w',encoding='gb2312')as f:
            f.write(html)

    def save_info(self,info):
        sql = 'insert into move_down values (%s,%s)'
        self.cursor.execute(sql,info[0])
        self.db.commit()

    def get_md5(self,link):
        m = md5()
        m.update(link.encode())
        return m.hexdigest()


    def run_spider(self):
        for i in range(1,11):
            one_url = self.url.format(3)
            one_html = self.get_html(one_url)
            # print(html)

            one_info = self.get_info(self.regix1,one_html)
            for url in one_info:
                second_url = 'https://www.dytt8.net' + url
                print(second_url)
                second_html = self.get_html(second_url)
                second_info = self.get_info(self.regix2,second_html)

                finger = self.get_md5(second_info[0][1])

                if self.r.sadd('move_fingers',finger):


                    self.save_info(second_info)
                else:
                    # self.cursor.close()
                    # self.db.close()
                    # sys.exit()
                    print('已存在')
                print(second_info[0])
                time.sleep(random.uniform(1,3))

        self.cursor.close()
        self.db.close()



if __name__ == '__main__':
    myspide = MoveSpider()
    myspide.run_spider()

# '<tbody><tr>.*?<a href="(.*?)" class="ulink">.*?</tbody>'
# https://www.dytt8.net/html/gndy/dyzz/20200217/59725.html