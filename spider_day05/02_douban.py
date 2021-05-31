import random
import re
import pymongo
import requests
from urllib import parse

import time
from fake_useragent import UserAgent

class DoubanSpider(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?type={}&interval_id=100:90&action=&start={}&limit=20'
        self.num_url = 'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100:90'
        self.count = 0
        self.conn = pymongo.MongoClient()
        self.db = self.conn['doubandb']
        self.myset = self.db['doubanset']

    def get_total(self,type):
        headers = {
            'User-Agent': UserAgent().random,
            # 'Referer':'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85%E7%89%87&type=11&interval_id=100:90&action=',
            # 'Cookie':'ll="108302"; bid=EHVvIcOdZB4; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1582522525%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DiMjAQ4TIKQvcMTCWD3U7f6IF_N2vBYUCYJqcf7Y3Wk2GpiOMMXW-LOWIsmJvno6P%26wd%3D%26eqid%3Dbd0d0d9e00008503000000035e53612f%22%5D; _pk_id.100001.4cf6=f012e1e1acf66b88.1582522525.1.1582523106.1582522525.; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.1827010698.1582522526.1582522526.1582522526.1; __utmb=30149280.0.10.1582522526; __utmc=30149280; __utmz=30149280.1582522526.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.113105164.1582522526.1582522526.1582522526.1; __utmb=223695111.0.10.1582522526; __utmc=223695111; __utmz=223695111.1582522526.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __yadk_uid=oYFVB2vnjyfEKOwplRTooDFYTOlKDJKQ'
        }

        url = self.num_url.format(type)
        res = requests.get(url=url, headers=headers)
        print(res.json()['total'])
        return res.json()['total']


    def get_html(self,type,start):

        headers = {
            'User-Agent':UserAgent().random,
            # 'Referer':'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85%E7%89%87&type=11&interval_id=100:90&action=',
            # 'Cookie':'ll="108302"; bid=EHVvIcOdZB4; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1582522525%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DiMjAQ4TIKQvcMTCWD3U7f6IF_N2vBYUCYJqcf7Y3Wk2GpiOMMXW-LOWIsmJvno6P%26wd%3D%26eqid%3Dbd0d0d9e00008503000000035e53612f%22%5D; _pk_id.100001.4cf6=f012e1e1acf66b88.1582522525.1.1582523106.1582522525.; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.1827010698.1582522526.1582522526.1582522526.1; __utmb=30149280.0.10.1582522526; __utmc=30149280; __utmz=30149280.1582522526.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.113105164.1582522526.1582522526.1582522526.1; __utmb=223695111.0.10.1582522526; __utmc=223695111; __utmz=223695111.1582522526.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __yadk_uid=oYFVB2vnjyfEKOwplRTooDFYTOlKDJKQ'
        }

        url = self.url.format(type,start)
        res = requests.get(url=url,headers = headers)

        for film in res.json():
            file_info = {}
            file_info['title']=film['title']
            file_info['score']=film['score']
            file_info['release_date']=film['release_date']
            print(file_info)
            self.myset.insert_one(file_info)
            self.count+=1

    def get_all_type(self):
        url = 'https://movie.douban.com/chart'
        headers = {
            'User-Agent':UserAgent().random,
            # 'Referer':'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85%E7%89%87&type=11&interval_id=100:90&action=',
            # 'Cookie':'ll="108302"; bid=EHVvIcOdZB4; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1582522525%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DiMjAQ4TIKQvcMTCWD3U7f6IF_N2vBYUCYJqcf7Y3Wk2GpiOMMXW-LOWIsmJvno6P%26wd%3D%26eqid%3Dbd0d0d9e00008503000000035e53612f%22%5D; _pk_id.100001.4cf6=f012e1e1acf66b88.1582522525.1.1582523106.1582522525.; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.1827010698.1582522526.1582522526.1582522526.1; __utmb=30149280.0.10.1582522526; __utmc=30149280; __utmz=30149280.1582522526.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.113105164.1582522526.1582522526.1582522526.1; __utmb=223695111.0.10.1582522526; __utmc=223695111; __utmz=223695111.1582522526.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __yadk_uid=oYFVB2vnjyfEKOwplRTooDFYTOlKDJKQ'
        }
        html = requests.get(url=url,headers = headers).text
        with open('aaa.html','w')as f:
            f.write(html)
        pattren = re.compile(r'type_name=(.*?)&type=(.*?)&',re.S)
        res = pattren.findall(html)
        # print(res)
        all_dict = dict(res)
        mnu = ''
        for key in all_dict:
            mnu = mnu +key +'|'
        print(mnu)
        return dict(res)

    def run(self):
        info_dict = self.get_all_type()
        for type in info_dict.values():
            # type = info_dict[input('请输入：')]
            total = self.get_total(type)
            for i in range(0,total,20):
                self.get_html(type,i)
                # time.sleep(random.uniform(1,3))
            print(self.count)

if __name__ == '__main__':
    myspider = DoubanSpider()
    myspider.run()