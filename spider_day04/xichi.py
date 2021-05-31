import random

import requests
import time
from fake_useragent import UserAgent
from lxml import etree


class XichiSpider(object):
    def __init__(self):
        self.url = "https://www.xicidaili.com/nn/{}"
        self.test_url = 'http://www.baidu.com'
        self.count=0

    def pase_html(self,page):
        full_url = self.url.format(page)
        headers = {
            'User-Agent':UserAgent().random
        }
        html = requests.get(url=full_url,headers = headers).text
        x_html = etree.HTML(html)
        # print(html)
        # ip_list = x_html.xpath('.//tbody/tr[position()>1]')
        ip_list = x_html.xpath('.//table/tr[position()>1]')
        for ip_item in ip_list:
            ip = ip_item.xpath('./td[2]/text()')[0]
            port = ip_item.xpath('./td[3]/text()')[0]
            type = ip_item.xpath('./td[6]/text()')[0].lower()
            # print(type,ip,port)
            self.verify(ip,port,type)


    def verify(self,ip,port,type):
        self.count += 1
        proxy = {
            type:type+'://'+ip+':'+port
        }
        headers = {
            'User-Agent': UserAgent().random
        }
        try:
            res = requests.get(self.test_url,proxies=proxy,headers=headers,timeout=3)
            print('第{}个：'.format(self.count),proxy, '\33[31m可用\033[0m')
            with open('proxy_success.txt', 'a')as f:
                f.write(proxy[type] + '\n')
        except Exception as e:
            with open('proxy_faile.txt', 'a')as f:
                f.write(proxy[type] + '\n')
            print('第{}个：'.format(self.count),proxy, '不可用')

    def run(self):
        for i in range(70,1000):
            self.pase_html(i)
            time.sleep(random.uniform(0.5,1))

if __name__ == '__main__':
    myspider = XichiSpider()
    myspider.run()