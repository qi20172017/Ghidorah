"""
使用独享代理来访问已经被封掉的西刺代理网站
"""
import requests

url = 'https://www.xicidaili.com/nn/1'
headers = {'User-Agent':'Mozilla/5.0'}
proxies = {
    'http':'http://309435365:szayclhp@49.7.96.227:16816',
    'https':'https://309435365:szayclhp@49.7.96.227:16816',
}
html = requests.get(url=url,proxies=proxies,headers=headers).text
print(html)



















