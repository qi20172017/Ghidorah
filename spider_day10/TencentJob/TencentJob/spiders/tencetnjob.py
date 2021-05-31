# -*- coding: utf-8 -*-
import scrapy
from ..items import TencentjobItem
import json
class TencetnjobSpider(scrapy.Spider):
    name = 'tencetnjob'
    allowed_domains = ['careers.tencent.com']
    # start_urls = ['http://careers.tencent.com/']

    def start_requests(self):
        for i in range(1,461,1):
        # for i in range(1,2,1):
            url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1582891930284&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'.format(i)
        # url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1582891930284&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=2&pageSize=10&language=zh-cn&area=cn'
        # url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1582891738220&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn'
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        data = json.loads(response.text)
        for item in data['Data']['Posts']:

            job_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1582892983865&postId={}&language=zh-cn'.format(item['PostId'])
            # job_url = 'https://careers.tencent.com/jobdesc.html?postId={}'.format(data['Data']['Posts'][0]['PostId'])
            # job_url = 'https://careers.tencent.com/jobdesc.html?postId={}'.format(item['PostId'])
            yield scrapy.Request(url=job_url,callback=self.parse_detail)

    def parse_detail(self,response):
        item = TencentjobItem()
        data = json.loads(response.text)
        item['name'] = data['Data']['RecruitPostName']
        item['address'] = data['Data']['LocationName']
        item['sort'] = data['Data']['CategoryName']
        item['time'] = data['Data']['LastUpdateTime']
        item['resp'] = data['Data']['Responsibility']
        item['require'] = data['Data']['Requirement']

        yield item
        # print(response.text)