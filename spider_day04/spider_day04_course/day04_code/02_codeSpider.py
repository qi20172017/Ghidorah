"""
抓取tedu的code,使用auth参数
"""
import requests
from lxml import etree
import os
from fake_useragent import UserAgent

class CodeSpider:
    def __init__(self):
        self.url = 'http://code.tarena.com.cn/AIDCode/aid1910/16_Spider/'
        self.auth = ('tarenacode','code_2013')
        self.directory = '/home/tarena/' + self.url[26:]
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def parse_html(self):
        headers = { 'User-Agent':UserAgent().random }
        html = requests.get(url=self.url,auth=self.auth,headers=headers).text
        p = etree.HTML(html)
        # href_list: ['../','day01/',...,'day01.zip']
        href_list = p.xpath('//a/@href')
        for href in href_list:
            if href.endswith('.zip'):
                # 下载1个文件的功能函数
                self.download_file(href)

    def download_file(self,href):
        """单独下载1个文件的功能函数"""
        down_link = self.url + href
        headers = { 'User-Agent':UserAgent().random }
        html = requests.get(url=down_link,auth=self.auth,headers=headers).content
        filename = self.directory + href
        with open(filename,'wb') as f:
            f.write(html)
        print(filename,'下载成功')

    def run(self):
        self.parse_html()

if __name__ == '__main__':
    spider = CodeSpider()
    spider.run()












