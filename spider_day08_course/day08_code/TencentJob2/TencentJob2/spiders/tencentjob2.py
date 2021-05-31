# -*- coding: utf-8 -*-
import scrapy
from ..items import Tencentjob2Item
from urllib import parse
import requests
import json

class Tencentjob2Spider(scrapy.Spider):
    name = 'tencentjob2'
    allowed_domains = ['careers.tencent.com']
    one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1566266592644&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
    two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1566266695175&postId={}&language=zh-cn'
    keyword = input('请输入职位类别：')

    keyword = parse.quote(keyword)

    def start_requests(self):
        total = self.get_total()
        for index in range(1,total+1,1):
            url = self.one_url.format(self.keyword,index)
            yield scrapy.Request(url=url,callback=self.parse)

    def get_total(self):
        """获取word类别的总页数"""
        url = self.one_url.format(self.keyword, 1)
        html = json.loads(self.get_html(url=url))
        count = html['Data']['Count']
        # 20个职位 : 2页 count//10
        # 25个职位 : 3页 count//10 + 1
        total = count // 10 if count % 10 == 0 else count // 10 + 1
        return total

    def get_html(self, url):
        """请求功能函数"""
        headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0',
                }
        html = requests.get(url=url, headers=headers).text
        return html

    def parse(self, response):

        html = json.loads(response.text)

        for one in html['Data']['Posts']:
            item = Tencentjob2Item()
            item['post_id'] = one['PostId']
            item['job_url'] = self.two_url.format(item['post_id'])
            yield scrapy.Request(url=item['job_url'],meta={'item':item},callback=self.detail_parse)

    def detail_parse(self,response):
        item = response.meta['item']
        # html = json.loads(response.text)
        data = json.loads(response.text)
        item['job_name'] = data['Data']['RecruitPostName']
        item['job_address'] = data['Data']['LocationName']
        item['job_type'] = data['Data']['CategoryName']
        item['job_time'] = data['Data']['LastUpdateTime']
        item['job_duty'] = data['Data']['Responsibility']
        item['job_require'] = data['Data']['Requirement']
        yield item
# job_name = scrapy.Field()
#     job_type = scrapy.Field()
#     job_duty = scrapy.Field()
#     job_require = scrapy.Field()
#     job_address = scrapy.Field()
#     job_time = scrapy.Field()
#     # 具体职位链接
#     job_url = scrapy.Field()
#     post_id = scrapy.Field()