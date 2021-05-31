from urllib import request
import random
import urllib


headers_pool = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
    'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50'
]

url = 'http://httpbin.org/get'
headers = {'User-Agent':random.choice(headers_pool)}
req = request.Request(url=url,headers=headers)
res = request.urlopen(req)
html = res.read().decode()
print(html)