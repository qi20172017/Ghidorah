import random

import requests
from hashlib import md5

import time
from fake_useragent import UserAgent

class YdSpider():
    def __init__(self):
        self.url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


    def get_html(self):
        headers = {
            # "Accept": "application/json, text/javascript, */*; q=0.01",
            # "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "OUTFOX_SEARCH_USER_ID=489094942@10.108.160.18; JSESSIONID=aaanBhujixFcYdvsmcSbx; OUTFOX_SEARCH_USER_ID_NCOO=1332477349.2848356; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcwwL4772JX6804McSbx; _ntes_nnid=71b5920eb28a2769877ffeb7e025c96c,1582360444396; ___rl__test__cookies=1582421551948",
            # "Host": "fanyi.youdao.com",
            # "Origin": "http://fanyi.youdao.com",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36",
            # "X-Requested-With": "XMLHttpRequest",
        }
        form_data = self.get_form_data()
        res = requests.post(self.url,data=form_data,headers=headers)
        print(res.text)

    def get_form_data(self):

        word = input('danci:')

        r = str(int(time.time()*1000))
        i = r + str(random.randint(0,9))
        ts = r
        str1 = "fanyideskweb" + word + i + "Nw(nmmbP%A-r6U3EUn]Aj"
        # str1 = "fanyideskweb" + word + i + "n%A-rKaT5fb[Gy?;N5@Tj"
        s = md5()
        s.update(str1.encode())
        sign = s.hexdigest()

        form_data = {
            "i": word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": i,
            "sign": sign,
            "ts": ts,
            "bv": "5158ae48583349ec7168cd8d4689c03e",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_CLICKBUTTION",
        }
        return form_data

    def run(self):
        self.get_html()

if __name__ == '__main__':
    myspider = YdSpider()
    myspider.run()