"""
抓取指定贴吧的指定页的数据
"""
from urllib import request,parse
import time
import random

class BaiduSpider:
    def __init__(self):
        """定义常用变量"""
        self.url = 'http://tieba.baidu.com/f?kw={}&pn={}'
        self.headers = {'User-Agent':'Mozilla/5.0'}

    # 请求函数 - 获取html
    def get_html(self,url):
        req = request.Request(url=url,headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode()

        return html

    # 解析提取数据 - 提取具体的数据
    def parse_html(self):
        pass

    # 保存数据: xxx吧_第x页.html
    def save_html(self,filename,html):
        with open(filename,'w') as f:
            f.write(html)

    # 程序入口函数
    def run(self):
        name = input('请输入贴吧名:')
        start_page = int(input('请输入起始页:'))
        end_page = int(input('请输入终止页:'))
        params = parse.quote(name)
        # 拼接url地址,发请求 解析 保存
        for page in range(start_page,end_page+1):
            pn = (page-1) * 50
            url = self.url.format(params,pn)
            html = self.get_html(url)
            filename = '{}_第{}页.html'.format(name,page)
            self.save_html(filename,html)
            print('第%d页抓取成功' % page)
            # 每抓取1页随机休眠1-2秒钟
            time.sleep(random.randint(1,2))

if __name__ == '__main__':
    spider = BaiduSpider()
    spider.run()


















