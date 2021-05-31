"""
把数据存入mysql数据库 - execute() 方法
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
        # 定义mysql相关变量
        self.db = pymysql.connect('localhost','root','123456','maoyandb',charset='utf8')
        self.cursor = self.db.cursor()

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
        ins = 'insert into maoyantab values(%s,%s,%s)'
        for film in film_list:
            # film: ('名称','主演','上映时间:2002(俄罗斯)'
            if film[2][9] == '(':
                li = [
                    film[0].strip(),
                    film[1].strip(),
                    film[2].strip()[5:9]
                ]
            else:
                li = [
                    film[0].strip(),
                    film[1].strip(),
                    film[2].strip()[5:15]
                ]
            self.cursor.execute(ins,li)
            self.db.commit()
            print(li)
            self.i += 1

    def run(self):
        """程序入口函数"""
        for offset in range(0,91,10):
            url = self.url.format(offset)
            self.get_html(url)
            # uniform:生成指定区间的浮点数
            time.sleep(random.uniform(0,1))
        # 断开数据库连接
        self.cursor.close()
        self.db.close()
        print('抓取数量:',self.i)

if __name__ == '__main__':
    start_time = time.time()
    spider = MaoyanSpider()
    spider.run()
    end_time = time.time()
    print('执行时间:%.2f' % (end_time-start_time))





















