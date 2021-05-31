import urllib.request

res = urllib.request.urlopen('http://httpbin.org/get')
print(res)
html = res.read()
url = res.geturl()
code = res.getcode()
print(code)
print(url)
print(html.decode())
