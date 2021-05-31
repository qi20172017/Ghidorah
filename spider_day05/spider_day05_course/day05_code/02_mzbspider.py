"""
行政区划代码抓取
"""
import requests
from lxml import etree
import re
import redis
from hashlib import md5
import sys

class MzbSpider:
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
        # 使用redis中集合做增量爬虫
        self.r = redis.Redis(host='localhost',port=6379,db=0)

    def get_html(self,url):
        """请求功能函数"""
        html = requests.get(url=url,headers=self.headers).text
        return html

    def xpath_func(self,html,xpath_bds):
        """xpath解析功能函数"""
        p = etree.HTML(html)
        r_list = p.xpath(xpath_bds)
        return r_list

    def md5_url(self,url):
        """md5加密功能函数"""
        s = md5()
        s.update(url.encode())
        return s.hexdigest()

    def parse_html(self):
        # 提取最新月份行政区划代码的链接
        html = self.get_html(self.url)
        xpath_bds = '//table/tr[2]/td[2]/a/@href'
        href_list = self.xpath_func(html,xpath_bds)
        if href_list:
            lasted_url = 'http://www.mca.gov.cn' + href_list[0]
            # 着手增量爬虫
            finger = self.md5_url(lasted_url)
            if self.r.sadd('mzb:fingers',finger):
                self.get_name_code(lasted_url)
            else:
                sys.exit('网站未更新')
        else:
            print('最新月份链接提取失败')

    def get_name_code(self,lasted_url):
        html = self.get_html(lasted_url)
        # 从html中提取新链接(真实返回数据的链接),此处进行了url地址的跳转
        regex = r'window.location.href="(.*?)"'
        pattern = re.compile(regex,re.S)
        real_link_list = pattern.findall(html)
        if real_link_list:
            real_url = real_link_list[0]
            # 向真实链接发请求,提取最终的数据
            self.get_data(real_url)
        else:
            print('真实链接提取失败')

    def get_data(self,real_url):
        """提取最终所需数据"""
        html = self.get_html(url=real_url)
        xpath_bds = '//tr[@height="19"]'
        tr_list = self.xpath_func(html,xpath_bds)
        for tr in tr_list:
            code_list = tr.xpath('./td[2]/text() | ./td[2]/span/text()')
            name_list = tr.xpath('./td[3]/text()')
            if code_list and name_list:
                code,name = code_list[0].strip(),name_list[0].strip()
                print(name,code)
            else:
                print(code_list,name_list)

    def run(self):
        self.parse_html()

if __name__ == '__main__':
    spider = MzbSpider()
    spider.run()














