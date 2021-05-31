import requests
from lxml import etree
from fake_useragent import UserAgent
import re

class CodeSpider():
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
        self.express1 = './/a[@title="2019年12月中华人民共和国县以上行政区划代码"]/@href'
        self.reexp= 'window.location.href="(.*?)";'

    def get_html(self):
        headers = {'UserAgent':UserAgent().random}
        html = requests.get(self.url,headers=headers)
        link = self.pass_html(html=html.text,express=self.express1)
        next_link = "http://www.mca.gov.cn"+link[0]
        print(next_link)
        html = requests.get(next_link,headers=headers)
        parttn = re.compile(self.reexp,re.S)
        info_link = parttn.findall(html.text)[0]

        html = requests.get(info_link, headers=headers)
        # info_list = self.pass_html(html.text,'.//tr')
        info_list = self.pass_html(html.text,'.//tr[@height=19]')
        for info  in info_list:
            code = info.xpath('./td[2]/text()')
            area = info.xpath('./td[3]/text()')
            print('area:{} code:{}'.format(area,code))
        # with open('res.html','w')as f:
        #     f.write(html.text)

    def run(self):
        self.get_html()

    def pass_html(self,html,express):
        x_html = etree.HTML(html)
        return x_html.xpath(express)

if __name__ == '__main__':
    myspider = CodeSpider()
    myspider.run()


# http://www.mca.gov.cn/article/sj/xzqh/2019/2019/202002191838.html