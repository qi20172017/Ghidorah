from urllib import request,parse


word = input('输入：')
url = 'http://www.baidu.com/s=?{}'.format(parse.urlencode({'wd':word}))
print(url)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50'
           }
req = request.Request(url=url,headers=headers)

res = request.urlopen(req)

html = res.read().decode()

file_name = word+'.html'
with open(file_name,'w',encoding='utf-8') as f:
    f.write(html)