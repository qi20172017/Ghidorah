"""
向测试网站发请求
"""
import requests

url = 'http://httpbin.org/get'
headers = { 'User-Agent':'xxxxxx' }

res = requests.get(url=url,headers=headers)
# 1.text: 获取响应内容-字符串
html = res.text
# 2.content: 获取响应内容-字节串
html = res.content
# 3.url: 返回实际数据的URL地址
url = res.url
# 4.status_code: 返回HTTP响应码
code = res.status_code
print(url,code)
































