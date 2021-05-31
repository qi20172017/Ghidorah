import requests
from fake_useragent import UserAgent
# url = 'http://httpbin.org/get'
url = 'https://esf.fang.com/house/i3{}/'
headers = {'User-Agent':UserAgent().random}
# proxies = {'http':'http://222.95.241.162:3000'}
# html = res.text
for i in range(2,10):
    res = requests.get(url=url.format(i),headers=headers)
    print(res.status_code)
    # print(html)
