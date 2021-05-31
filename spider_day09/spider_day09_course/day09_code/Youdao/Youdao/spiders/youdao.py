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
        cookies = self.get_cookies()
        # 交给调度器入队列 - FormRequest()方法
        yield scrapy.FormRequest(
            # 此处注意cookies参数,因为settings.py中 COOKIES_ENABLED = True
            url=post_url,formdata=formdata,callback=self.parse,cookies=cookies
        )

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

    def get_cookies(self):
        string = 'OUTFOX_SEARCH_USER_ID=970246104@10.169.0.83; OUTFOX_SEARCH_USER_ID_NCOO=570559528.1224236; _ntes_nnid=96bc13a2f5ce64962adfd6a278467214,1551873108952; JSESSIONID=aaae9i7plXPlKaJH_gkYw; td_cookie=18446744072941336803; SESSION_FROM_COOKIE=unknown; ___rl__test__cookies=1565689460872'
        cookies = {}
        for kv in string.split('; '):
            key = kv.split('=')[0]
            value = kv.split('=')[1]
            cookies[key] = value

        return cookies

    def parse(self, response):
        html = json.loads(response.text)
        # 创建item对象
        item = YoudaoItem()
        item['result'] = html['translateResult'][0][0]['tgt']

        yield item
