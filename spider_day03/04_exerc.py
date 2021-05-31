"""
初始程序 - 抓取猫眼电影top100,终端打印输出字典
"""
from lxml import etree
import requests
import re
import time
import random

class MaoyanSpider:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
        }

        # 计数
        self.i = 0

    def get_html(self,url):
        html = requests.get(url=url,headers=self.headers).text
        # 直接解析提取数据
        self.parse_html(html)

    def parse_html(self,html):
        """提取数据函数"""
        xhtml = etree.HTML(html)
        film_list = xhtml.xpath('.//dl[@class="board-wrapper"]/dd')

        for film in film_list:
            info_dir={}
            info_dir['name'] = film.xpath('./a/@title')[0].strip()
            info_dir['star'] = film.xpath('.//p[@class="star"]/text()')[0].strip()
            info_dir['time'] = film.xpath('.//p[@class="releasetime"]/text()')[0].strip()
            # 直接调用数据处理函数
            # self.save_html(film_list)
            print(info_dir)
    def save_html(self,film_list):
        """处理数据函数"""
        item = {}
        for film in film_list:
            item['name'] = film[0].strip()
            item['star'] = film[1].strip()
            item['time'] = film[2].strip()
            print(item)
            self.i += 1

    def run(self):
        """程序入口函数"""
        for offset in range(0,91,10):
            url = self.url.format(offset)
            self.get_html(url)
            # uniform:生成指定区间的浮点数
            time.sleep(random.uniform(0,1))
        print('抓取数量:',self.i)

if __name__ == '__main__':
    start_time = time.time()
    spider = MaoyanSpider()
    spider.run()
    end_time = time.time()
    print('执行时间:%.2f' % (end_time-start_time))

