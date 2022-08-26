import scrapy


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['www.guazi.com']
    start_urls = ['http://www.guazi.com/']

    def parse(self, response):
        pass
