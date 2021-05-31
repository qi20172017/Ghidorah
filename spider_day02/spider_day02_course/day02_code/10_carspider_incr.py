"""
抓取汽车之家二手车信息,用mysql实现增量爬虫
"""
from urllib import request
import re
import time
import random
import pymysql
from hashlib import md5
import sys

class CarSpider:
    def __init__(self):
        self.one_url = 'https://www.che168.com/beijing/a0_0msdgscncgpi1lto1csp{}exx0/'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
        # MySQL相关变量
        self.db = pymysql.connect('localhost','root','123456','cardb',charset='utf8')
        self.cursor = self.db.cursor()

    # 功能函数1 - 获取html
    def get_html(self,url):
        req = request.Request(url=url,headers=self.headers)
        try:
            res = request.urlopen(req,timeout=5)
            html = res.read().decode('gb2312','ignore')
            return html
        except Exception as e:
            print(e)

    # 功能函数2 - 正则解析
    def re_func(self,regex,html):
        pattern = re.compile(regex,re.S)
        r_list = pattern.findall(html)

        return r_list

    # 功能函数3 - md5加密
    def md5_func(self,string):
        s = md5()
        s.update(string.encode())

        return s.hexdigest()

    # 爬虫开始
    def parse_html(self,one_url):
        # 1.先从一级页面的响应中提取所有汽车的链接
        one_html = self.get_html(one_url)
        one_regex = '<li class="cards-li list-photo-li".*?<a href="(.*?)".*?</li>'
        # href_list: ['/delear/xx/xx','/delear/xxx/xx','']
        href_list = self.re_func(one_regex,one_html)
        # 2.依次向汽车详情页链接发请求,获取具体的数据
        for href in href_list:
            # 一辆汽车的完整链接
            two_url = 'https://www.che168.com' + href
            finger = self.md5_func(two_url)
            # 判断finger是否存在: 表中存在(False) 表中不存在(True)
            if self.go_spider(finger):
                self.get_car_info(two_url)
                time.sleep(random.uniform(1,2))
                # 抓取完后把finger存入到指纹表
                ins = 'insert into request_finger values(%s)'
                self.cursor.execute(ins,[finger])
                self.db.commit()
            else:
                sys.exit('更新完成')

    def go_spider(self,finger):
        """判断finger是否存在: 表中存在(False) 表中不存在(True)"""
        sel = 'select finger from request_finger where finger=%s'
        self.cursor.execute(sel,[finger])
        result = self.cursor.fetchone()
        if result:
            return False
        return True

    def get_car_info(self,two_url):
        """获取1辆汽车的详情数据"""
        two_html = self.get_html(two_url)
        two_regex = '<div class="car-box">.*?<h3 class="car-brand-name">(.*?)</h3>.*?<ul class="brand-unit-item fn-clear">.*?<li>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<span class="price" id="overlayPrice">￥(.*?)<b'
        car_info_list = self.re_func(two_regex,two_html)
        # car_info_list:
        # [('五菱荣光','3万公里','2017年','手动/1.5L','廊坊','3.6'),]
        item = {}
        item['name'] = car_info_list[0][0]
        item['km'] = car_info_list[0][1]
        item['year'] = car_info_list[0][2]
        item['type'] = car_info_list[0][3].split('/')[0]
        item['displace'] = car_info_list[0][3].split('/')[1]
        item['city'] = car_info_list[0][4]
        item['price'] = car_info_list[0][5]
        print(item)

    def run(self):
        for i in range(1,5):
            one_url = self.one_url.format(i)
            self.parse_html(one_url)

if __name__ == '__main__':
    spider = CarSpider()
    spider.run()










