# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from fake_useragent import UserAgent
from .proxypool import proxy_list


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

        # Should return either None or an iterable of Request, dict
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


class BaiduUaDownloaderMiddleware(object):
    def process_request(self,request,spider):
        agent = UserAgent().random
        request.headers['User-Agent'] = agent
        print('middleware:',agent)

import random
class BaiduProxyDownloaderMiddleware(object):
    def process_request(self,request,spider):
        proxy = random.choice(proxy_list)
        request.meta['proxy'] = proxy
        print(proxy)

    def process_exception(self, request, exception, spider):
        return request

class BaiduCookieDownloaderMiddleware(object):
    def process_request(self,request,spider):
        cookie_dic = self.get_cookie()
        request.cookies = cookie_dic
        print(cookie_dic)

    def get_cookie(self):
        cookie_str = "BAIDUID=751F392F1100F41683F45D49245DE2B2:FG=1; BIDUPSID=751F392F1100F41683F45D49245DE2B2; PSTM=1509104901; BD_UPN=133352; BDUSS=VFVR0Rib2tsYlJDTX5RTWlkQTU2U1E0VXJzZEdEcUphNjB0d1pib0FFOFAtV2hlRVFBQUFBJCQAAAAAAAAAAAEAAAAn9pw0v8m~v7XEbWlubWluNQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA9sQV4PbEFed; COOKIE_SESSION=75480_0_7_2_17_17_0_0_2_7_157_3_75480_0_160_0_1582966802_0_1582966642%7C9%230_1_1582351547%7C1; BD_HOME=1; H_PS_PSSID=1442_21125_30793_30906_30824_26350"
        cookie_dir = {}
        for kv in cookie_str.split('; '):
            cookie_dir[kv.split('=')[0]] = kv.split('=')[1]
        return cookie_dir