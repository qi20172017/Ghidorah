"""
初始程序 - 抓取猫眼电影top100,终端打印输出字典
"""
from lxml import etree
import requests
import re
import time
import random
from fake_useragent import UserAgent
class MaoyanSpider:
    def __init__(self):
        self.url = 'https://sh.lianjia.com/ershoufang/pg{}/'


        # 计数
        self.i = 0

    def get_html(self,url):
        headers = {
            'User-Agent':UserAgent().random
        }
        html = requests.get(url=url,headers=headers).text
        # 直接解析提取数据
        self.parse_html(html)

    def parse_html(self,html):
        """提取数据函数"""
        xhtml = etree.HTML(html)
        film_list = xhtml.xpath('.//ul[@log-mod="list"]/li[contains(@class,"clear")]/div[@class="info clear"]')

        for film in film_list:
            info_dir={}
            info_dir['name'] = film.xpath('./div[@class="title"]/a/text()')[0].strip()
            info_dir['flood'] = '-'.join(film.xpath('./div[@class="flood"]//a/text()'))
            info_dir['address'] = film.xpath('./div[@class="address"]/div/text()')[0].strip()
            info_dir['totalPrice'] = film.xpath('./div[@class="priceInfo"]/div[1]/span/text()')[0].strip()
            info_dir['singlePrice'] = film.xpath('./div[@class="priceInfo"]/div[2]/span/text()')[0].strip()
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
            time.sleep(random.uniform(1,3))
        print('抓取数量:',self.i)

if __name__ == '__main__':
    start_time = time.time()
    spider = MaoyanSpider()
    spider.run()
    end_time = time.time()
    print('执行时间:%.2f' % (end_time-start_time))

