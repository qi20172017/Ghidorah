# -*- coding: utf-8 -*-
import scrapy
import time
from hashlib import md5
import random
import json
from ..items import YoudaoItem

class YoudaoSpider(scrapy.Spider):
    name = 'youdao'
    allowed_domains = ['fanyi.youdao.com']
    word = input('请输入要翻译的单词:')

    # POST请求必须重写 start_requests() 方法
    def start_requests(self):
        """把POST的URL地址、Form表单数据交给调度器入队列"""
        post_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        salt,sign,ts = self.get_salt_sign_ts()
        formdata = {
            'i': self.word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'ts': ts,
            'bv': 'cf156b581152bd0b259b90070b1120e6',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }
        # 交给调度器入队列 - FormRequest()方法
        yield scrapy.FormRequest(
            url=post_url,formdata=formdata,callback=self.parse)

    def get_salt_sign_ts(self):
        """获取salt、sign、ts"""
        # salt
        salt = str(int(time.time() * 1000)) + str(random.randint(0, 9))
        # sign
        string = "fanyideskweb" + self.word + salt + "n%A-rKaT5fb[Gy?;N5@Tj"
        s = md5()
        s.update(string.encode())
        sign = s.hexdigest()
        # ts
        ts = str(int(time.time() * 1000))
        return salt, sign, ts


    def parse(self, response):
        html = json.loads(response.text)
        # 创建item对象
        item = YoudaoItem()
        item['result'] = html['translateResult'][0][0]['tgt']

        yield item
