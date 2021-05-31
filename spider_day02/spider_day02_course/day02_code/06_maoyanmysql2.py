"""
使用executemany()方法存入数据库
"""
from urllib import request
import re
import time
import random
import pymysql

class MaoyanSpider:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
        }
        # 计数
        self.i = 0
        self.db = pymysql.connect('localhost','root','123456','maoyandb',charset='utf8')
        self.cursor =self.db.cursor()
        # 存放所有电影信息的大列表 [(),(),(),(),...,()]
        self.all_list = []

    def get_html(self,url):
        req = request.Request(url=url,headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8','ignore')
        # 直接解析提取数据
        self.parse_html(html)

    def parse_html(self,html):
        """提取数据函数"""
        regex = '<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>'
        pattern = re.compile(regex,re.S)
        # film_list: [('霸王别姬','张国荣','1993'),()]
        film_list = pattern.findall(html)
        # 直接调用数据处理函数
        self.save_html(film_list)

    def save_html(self,film_list):
        """处理数据函数"""
        for film in film_list:
            if film[2][9] == '(':
                film_t = (film[0].strip(),film[1].strip(),film[2].strip()[5:9])
            else:
                film_t = (film[0].strip(), film[1].strip(), film[2].strip()[5:15])
            # 把每个电影信息的元组添加到大列表中
            self.all_list.append(film_t)
            print(film_t)
            self.i += 1

    def run(self):
        """程序入口函数"""
        for offset in range(0,91,10):
            url = self.url.format(offset)
            self.get_html(url)
            # uniform:生成指定区间的浮点数
            time.sleep(random.uniform(0,1))
        # 使用executemany()方法一次性插入所有数据
        ins = 'insert into maoyantab values(%s,%s,%s)'
        self.cursor.executemany(ins,self.all_list)
        self.db.commit()
        self.cursor.close()
        self.db.close()
        print('抓取数量:',self.i)

if __name__ == '__main__':
    start_time = time.time()
    spider = MaoyanSpider()
    spider.run()
    end_time = time.time()
    print('执行时间:%.2f' % (end_time-start_time))





















