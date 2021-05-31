"""
抓取图片 - 非结构化数据抓取和保存
保存路径: /home/tarena/baiduimage/赵丽颖/
"""
import requests
import os

# 创建对应文件夹
directory = '/home/tarena/baiduimage/赵丽颖/'
if not os.path.exists(directory):
    os.makedirs(directory)

url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1582259539649&di=4cbf26ec9b7e5731df80345d4858c5b5&imgtype=0&src=http%3A%2F%2Fimg2.17getfun.com%2FtaY-t1MBYBvaW9c.JPEG'
headers = {'User-Agent':'Mozilla/5.0'}

html = requests.get(url=url,headers=headers).content
# 问题1: 解决文件名的问题
# filename: /home/tarena/baiduimage/赵丽颖/xxxx.jpeg
filename = directory + url[-10:]
with open(filename,'wb') as f:
    f.write(html)

print('ok')





