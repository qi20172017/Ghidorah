import requests
import os
url = 'http://pic1.win4000.com/wallpaper/b/4fcdd4df638d1.jpg'
# url = 'http://httpbin.org/get'
res = requests.get(url)
# print(res.content)
file_name = url[-15:]



with open(file_name,'wb')as f:
    f.write(res.content)
# print(file_name)