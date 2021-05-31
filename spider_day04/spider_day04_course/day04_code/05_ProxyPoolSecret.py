"""
使用私密代理
"""
import requests

class ProxyPool:
    def __init__(self):
        self.api_url = 'http://dps.kdlapi.com/api/getdps/?orderid=988235447954268&num=20&pt=1&sep=1'
        self.test_url = 'http://www.baidu.com/'
        self.headers = {'User-Agent':'Mozilla/5.0'}
        self.f = open('proxy.txt','a')

    def get_proxy(self):
        """获取代理IP"""
        html = requests.get(url=self.api_url,headers=self.headers).text
        # proxy_list: ['1.1.1.1:8888','2.2.2.2:9999',...]
        proxy_list = html.split('\r\n')
        for proxy in proxy_list:
            self.test_proxy(proxy)

    def test_proxy(self,proxy):
        """测试1个代理IP是否可用"""
        proxies = {
            'http' : 'http://309435365:szayclhp@{}'.format(proxy),
            'https': 'https://309435365:szayclhp@{}'.format(proxy)
        }
        try:
            res = requests.get(url=self.test_url,proxies=proxies,headers=self.headers,timeout=3)
            print(proxy,'\33[31m可用\033[0m')
            self.f.write(proxy + '\n')
        except Exception as e:
            print(proxy,'不可用')

    def run(self):
        self.get_proxy()

if __name__ == '__main__':
    spider = ProxyPool()
    spider.run()











