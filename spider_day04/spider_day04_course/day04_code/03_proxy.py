"""
使用代理IP访问测试网站
"""
import requests

url = 'http://httpbin.org/get'
headers = {'User-Agent':'xxxxx'}
proxies = {
    'http' : 'http://171.35.143.35:9999',
    'https' : 'https://171.35.143.35:9999',
}
html = requests.get(url=url,proxies=proxies,headers=headers).text
print(html)

"""
代理IP异常有两种:
1. 连不上代理IP: 瞬间抛出异常ProxyError
2. 连接上了代理IP,但是代理IP不能访问网站: 等待
"""











