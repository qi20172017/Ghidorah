# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class BaiduSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class BaiduDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

# 中间件1 - 包装随机User-Agent
from fake_useragent import UserAgent

class BaiduUaDownloaderMiddleware(object):
    def process_request(self, request, spider):
        # request 为被拦截下来的请求对象,利用headers属性设置
        agent = UserAgent().random
        request.headers['User-Agent'] = agent
        print('middlewares1:',agent)

# 中间件2 - 包装随机代理IP
from .proxypool import proxy_list
import random

class BaiduProxyDownloaderMiddleware(object):
    def process_request(self, request, spider):
        # 利用meta属性,定义代理
        proxy = random.choice(proxy_list)
        request.meta['proxy'] = proxy
        print('middlewares2',proxy)

    # 代理IP不稳定,尝试3次后scrapy会抛出异常,所以要捕获
    def process_exception(self, request, exception, spider):
        return request

# 中间件3 - 添加cookie
class BaiduCookieDownloadMiddlleware(object):
    def process_request(self, request, spider):
        # 添加cookies：利用request.cookies属性
        cookies_dict = self.get_cookie()
        request.cookies = cookies_dict
        print('middlewares3',cookies_dict)

    def get_cookie(self):
        costr = 'BIDUPSID=452BDC861D9B7AE8C40F5EA5E4099D76; PSTM=1582875696; BAIDUID=452BDC861D9B7AE83D64B83E4F22005B:FG=1; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; COOKIE_SESSION=18529_0_7_0_8_21_0_0_0_7_1_0_0_0_4_0_1583034521_0_1583053046%7C7%230_0_1583053046%7C1; BD_HOME=1; H_PS_PSSID=1457_21098_30839_30824_26350_30717'
        cookies = {}
        for kv in costr.split('; '):
            cookies[kv.split('=')[0]] = kv.split('=')[1]

        return cookies



