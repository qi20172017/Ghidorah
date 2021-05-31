"""
让西刺代理封掉我的IP！！！
"""
import requests

url = 'https://www.xicidaili.com/nn/{}'
headers = {'User-Agent':'Mozilla/5.0'}
for i in range(1,101):
    url = url.format(i)
    res = requests.get(url=url,headers=headers)
    print(res.status_code)
    print(i)
