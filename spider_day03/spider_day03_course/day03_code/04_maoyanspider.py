"""
初始程序 - 抓取猫眼电影top100,终端打印输出字典
"""
import requests
from lxml import etree
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
        # 1.创建解析对象
        p = etree.HTML(html)
        # 基准xpath,得到十个dd节点对象的列表
        # dd_list: [<element dd at xx>,<element dd at xxx>]
        dd_list = p.xpath('//dl[@class="board-wrapper"]/dd')
        item = {}
        for dd in dd_list:
            item['name'] = dd.xpath('.//p[@class="name"]/a/text()')[0].strip()
            item['star'] = dd.xpath('.//p[@class="star"]/text()')[0].strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()')[0].strip()
            print(item)


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





















