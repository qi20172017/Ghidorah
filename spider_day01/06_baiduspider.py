import random
from urllib import request,parse
import time
class BaiduSpider:
    def __init__(self):

        self.url = 'http://tieba.baidu.com/f?kw={}&pn={}'
        self.headers = headers = {'User-Agent':'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
           }


    def get_html(self,url):
        req = request.Request(url,headers=self.headers)
        res = request.urlopen(req)
        print(res.geturl())
        html = res.read().decode()
        return html

    def parse_html(self):
        pass

    def save_html(self,filename,html):
        with open(filename,'w') as f:
            f.write(html)


    def run(self):
        name = input('请输入贴吧名字：')
        start_page = int(input('请输入起始页：'))
        end_page = int(input('请输入终止页：'))
        params = parse.quote(name)
        for page in range(start_page,end_page+1):
            full_url = self.url.format(params,(page-1)*50)
            html = self.get_html(full_url)
            filename = name + '吧第{}页.html'.format(page)
            self.save_html(filename,html)
            print('第%s页抓取成功'%page)
            time.sleep(random.randint(1,3))
if __name__ == '__main__':
    spider = BaiduSpider()
    spider.run()
