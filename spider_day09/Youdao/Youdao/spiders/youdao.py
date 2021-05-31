# -*- coding: utf-8 -*-
import scrapy
import time
import random
from hashlib import md5
import json
from ..items import YoudaoItem


class YoudaoSpider(scrapy.Spider):
    name = 'youdao'
    allowed_domains = ['fanyi.youdao.com']
    # start_urls = ['http://fanyi.youdao.com/']
    word = input('请输入单词：')
    def start_requests(self):
        salt, sign, ts = self.get_salt_sign_ts(self.word)
        cookies = self.get_cookie()
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
        post_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        yield scrapy.FormRequest(url=post_url,formdata=formdata,callback=self.parse,cookies=cookies)

    def get_cookie(self):
        cookie = "OUTFOX_SEARCH_USER_ID=970246104@10.169.0.83; OUTFOX_SEARCH_USER_ID_NCOO=570559528.1224236; _ntes_nnid=96bc13a2f5ce64962adfd6a278467214,1551873108952; JSESSIONID=aaae9i7plXPlKaJH_gkYw; td_cookie=18446744072941336803; SESSION_FROM_COOKIE=unknown; ___rl__test__cookies=1565689460872"
        cookie_dir = {}
        for kv in cookie.split('; '):
            res = kv.split('=')
            cookie_dir[res[0]] = res[1]
        return cookie_dir



    def get_salt_sign_ts(self, word):
        # salt
        salt = str(int(time.time() * 1000)) + str(random.randint(0, 9))
        # sign
        string = "fanyideskweb" + word + salt + "n%A-rKaT5fb[Gy?;N5@Tj"
        s = md5()
        s.update(string.encode())
        sign = s.hexdigest()
        # ts
        ts = str(int(time.time() * 1000))
        return salt, sign, ts

    def parse(self, response):
        data = json.loads(response.text)
        item = YoudaoItem()
        item['result'] = data['translateResult'][0][0]['tgt']
        yield item
