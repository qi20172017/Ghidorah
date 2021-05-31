import requests

baseurl = 'https://www.baidu.com/s?'
params = {
    'wd':'python'
}

res = requests.get(url=baseurl,params=params)
html = res.text()
print()
with open('badi.html','w')as f:
    f.write(html)