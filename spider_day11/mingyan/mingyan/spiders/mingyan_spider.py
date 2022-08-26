import scrapy


class Mingyan(scrapy.Spider):
    name = "mingyan"

    # start_urls = [
    #     "http://lab.scrapyd.cn/page/1/",
    #     "http://lab.scrapyd.cn/page/2/",
    # ]

    # def start_requests(self):
    #     urls = [
    #         "http://lab.scrapyd.cn/page/1/",
    #         "http://lab.scrapyd.cn/page/2/",
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=(self.parse))

    def start_requests(self):
        url = 'http://lab.scrapyd.cn/'
        tag = getattr(self, 'tag', None)  # 获取tag值，也就是爬取时传过来的参数
        if tag is not None:  # 判断是否存在tag，若存在，重新构造url
            url = url + 'tag/' + tag  # 构造url若tag=爱情，url= "http://lab.scrapyd.cn/tag/爱情"
        yield scrapy.Request(url, self.parse)  # 发送请求爬取参数内容



    def parse(self, response, **kwargs):
        # page = response.url.split("/")[-2]
        # self.log("保存文件:%s" % page)

        mingyan = response.css('div.quote')  # 提取首页所有名言，保存至变量mingyan

        for v in mingyan:  # 循环获取每一条名言里面的：名言内容、作者、标签

            text = v.css('.text::text').extract_first()  # 提取名言
            autor = v.css('.author::text').extract_first()  # 提取作者
            tags = v.css('.tags .tag::text').extract()  # 提取标签
            tags = ','.join(tags)  # 数组转换为字符串


            self.log(text)
            self.log(autor)
            self.log(tags)

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)  # 关键在这一句，这个就是发送的将要爬取的请求