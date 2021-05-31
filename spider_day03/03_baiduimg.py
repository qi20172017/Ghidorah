import random
from lxml import etree
import requests
import os
import re
import time
from urllib import parse
# path = '/home/tarena/images'

class BaiduImage:
    def __init__(self):
        self.url = 'https://image.baidu.com/search/index?tn=baiduimage&word={}'
        self.headers = {'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0"}
        self.i = 1
        self.word = input('输入：')
        self.directory = '/home/tarena/images/{}/'.format(self.word)
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def get_img(self):

        url = self.url.format(parse.quote(self.word))
        html = requests.get(url=url,headers=self.headers).text

        regex = '"thumbURL":"(.*?)"'
        pattern = re.compile(regex)
        src_list = pattern.findall(html)
        for src in src_list:
            print(src)
            self.save_img(src)
            time.sleep(random.uniform(2,4))

    def save_img(self,src):
        html = requests.get(url=src,headers=self.headers).content
        filename = '{}{}{}'.format(self.directory,self.word,self.i)
        with open(filename,'wb')as f:
            f.write(html)

        self.i += 1
    def run(self):
        self.get_img()
if __name__ == '__main__':
    myspider = BaiduImage()
    myspider.run()