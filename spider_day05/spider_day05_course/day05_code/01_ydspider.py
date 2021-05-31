"""
爬取有道翻译的翻译结果
"""
import requests
import time
import random
from hashlib import md5

class YdSpider:
    def __init__(self):
        # post_url: F12抓包抓到的POST的地址
        self.post_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            # 网站检查频率很高的headers中的三个字段: Cookie Referer User-Agent
            "Cookie": "OUTFOX_SEARCH_USER_ID=-339493990@10.168.1.247; OUTFOX_SEARCH_USER_ID_NCOO=2102460643.9014387; JSESSIONID=aaaETXDBnE2YjcYpPZ0bx; ___rl__test__cookies=1582507720984",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
        }

    def get_salt_sign_ts(self,word):
        """获取表单数据中的salt sign ts"""
        ts = str(int(time.time()*1000))
        salt = ts + str(random.randint(0,9))
        string = "fanyideskweb" + word + salt + "n%A-rKaT5fb[Gy?;N5@Tj"
        s = md5()
        s.update(string.encode())
        sign = s.hexdigest()

        return salt,sign,ts

    def attack_yd(self,word):
        # 把form表单数据post到 self.post_url ,获取响应内容
        salt,sign,ts = self.get_salt_sign_ts(word)
        # 检查频率最高: salt sign
        data = {
            "i": word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "ts": ts,
            "bv": "887ddef35bb193fe341b77b7709d1160",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }
        # .json() 把json格式的字符串转为python数据类型
        html = requests.post(url=self.post_url,data=data,headers=self.headers).json()
        result = html["translateResult"][0][0]["tgt"]

        return result

    def run(self):
        word = input('请输入要翻译的单词:')
        result = self.attack_yd(word)
        print('翻译结果：',result)

if __name__ == '__main__':
    spider = YdSpider()
    spider.run()






