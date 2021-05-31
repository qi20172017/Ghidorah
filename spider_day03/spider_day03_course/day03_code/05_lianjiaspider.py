"""
lxml+xpath提取链家二手房信息
"""
import requests
from lxml import etree
import time
import random
from fake_useragent import UserAgent

class LianjiaSpider:
    def __init__(self):
        self.url = 'https://bj.lianjia.com/ershoufang/pg{}/'

    def get_html(self,url):
        """爬虫函数,一定要把headers定义在此函数中"""
        headers = {'User-Agent': UserAgent().random}
        # 遇到未响应页面等待3秒钟,尝试3次,都不行则抓取下一页数据
        for i in range(3):
            try:
                html = requests.get(url=url,headers=headers,timeout=3).text
                self.parse_html(html)
                break
            except Exception as e:
                print('Retry')

    def parse_html(self,html):
        """解析提取数据"""
        p = etree.HTML(html)
        # 先写基准xpath表达式,然后再for循环依次遍历
        # li_list: [<element li at xx>,<element li at xxx>,...]
        li_list = p.xpath('//ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
        item = {}
        for li in li_list:
            # 名称+区域
            name_list = li.xpath('.//div[@class="positionInfo"]/a[1]/text()')
            item['name'] = name_list[0].strip() if name_list else None
            add_list = li.xpath('.//div[@class="positionInfo"]/a[2]/text()')
            item['add'] = add_list[0].strip() if add_list else None
            # 户型+面积+方位+是否精装+楼层+年代+类型
            # hinfo_list: ['两室一厅 | 88 | 南北 | xxx | xxx']
            hinfo_list = li.xpath('.//div[@class="houseInfo"]/text()')
            if hinfo_list:
                hinfo_list = hinfo_list[0].split('|')
                item['model'] = hinfo_list[0].strip()
                item['area'] = hinfo_list[1].strip()
                item['direct'] = hinfo_list[2].strip()
                item['perfect'] = hinfo_list[3].strip()
                item['floor'] = hinfo_list[4].strip()
                item['year'] = hinfo_list[5].strip()
                item['type'] = hinfo_list[6].strip()
            else:
                item['model']=item['area']=item['direct']=item['perfect']=item['floor']=item['year']=item['type'] = None
            # 总价+单价
            total_list = li.xpath('.//div[@class="totalPrice"]/span/text()')
            item['total'] = total_list[0].strip() if total_list else None
            unit_list = li.xpath('.//div[@class="unitPrice"]/span/text()')
            item['unit'] = unit_list[0].strip() if unit_list else None

            print(item)

    def run(self):
        for pg in range(1,101):
            url = self.url.format(pg)
            self.get_html(url)
            time.sleep(random.uniform(0,2))

if __name__ == '__main__':
    spider = LianjiaSpider()
    spider.run()


















