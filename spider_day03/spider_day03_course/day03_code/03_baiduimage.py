"""
抓取百度图片的首页30张图片,保存到 /home/tarena/images/关键字/xxx.jpg
"""
import requests
from urllib import parse
import re
import os
import time
import random

class BaiduImage:
    def __init__(self):
        self.url = 'https://image.baidu.com/search/index?tn=baiduimage&word={}'
        self.headers = {'User-Agent':'Mozilla/5.0'}
        # 用于图片命名
        self.i = 1
        self.word = input('请输入关键字:')
        self.directory = '/home/tarena/images/{}/'.format(self.word)
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def get_image(self):
        # 1.拼接url地址,发请求获取响应内容
        params = parse.quote(self.word)
        url = self.url.format(params)
        html = requests.get(url=url,headers=self.headers).text
        # 2.正则解析提取30张图片链接
        regex = '"thumbURL":"(.*?)"'
        pattern = re.compile(regex,re.S)
        src_list = pattern.findall(html)
        # src_list: ['http://x1.jpg','http://x2.jpg','','']
        for src in src_list:
            # 函数功能: 把1张图片保存到本地
            self.save_image(src)
            time.sleep(random.uniform(0,1))

    def save_image(self,src):
        """保存1张图片到本地"""
        html = requests.get(url=src,headers=self.headers).content
        # filename: /home/tarena/images/赵丽颖/赵丽颖1.jpg
        filename = '{}{}{}.jpg'.format(self.directory,self.word,self.i)
        with open(filename,'wb') as f:
            f.write(html)
        self.i += 1
        print(filename,'下载成功')

    def run(self):
        self.get_image()

if __name__ == '__main__':
    spider = BaiduImage()
    spider.run()









