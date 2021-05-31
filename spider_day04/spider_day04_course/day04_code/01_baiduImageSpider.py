"""
抓取指定贴吧的所有帖子中的图片
"""
import requests
from lxml import etree
import time
import random
from urllib import parse

class TiebaImageSpider:
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?kw={}&pn={}'
        # IE的User-Agent返回数据最标准,如果数据出不来,可考虑使用IE的请求头尝试
        # 极少数网站,其他几乎所有还是以响应内容为准
        self.headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}

    def get_html(self,url):
        """请求功能函数"""
        html = requests.get(url=url,headers=self.headers).text

        return html

    def xpath_func(self,html,xbds):
        """解析功能函数"""
        p = etree.HTML(html)
        r_list = p.xpath(xbds)

        return r_list

    def parse_html(self,one_url):
        """主线函数,爬虫的开始"""
        one_html = self.get_html(one_url)
        one_xbds = '//div[@class="t_con cleafix"]/div/div/div/a/@href'
        # href_list: ['/p/23232/','/p/09028']
        href_list = self.xpath_func(one_html,one_xbds)
        for href in href_list:
            t_link = 'http://tieba.baidu.com' + href
            # 要把此帖子中所有的图片保存到本地
            self.save_images(t_link)

    def save_images(self,t_link):
        """把1个帖子中所有的图片保存到本地
           向帖子链接发请求,提取图片链接,再依次向图片链接发请求保存
        """
        two_html = self.get_html(t_link)
        two_xbds = '//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src | //div[@class="video_src_wrapper"]/embed/@data-video'
        img_link_list = self.xpath_func(two_html,two_xbds)
        for img_link in img_link_list:
            # 把1张图片保存到本地
            self.save_one_img(img_link)
            time.sleep(random.uniform(0,1))

    def save_one_img(self,img_link):
        """保存1张图片到本地"""
        img_html = requests.get(url=img_link,headers=self.headers).content
        filename = img_link[-10:]
        with open(filename,'wb') as f:
            f.write(img_html)
        print(filename,'下载成功')

    def run(self):
        name = input('请输入贴吧名:')
        start = int(input('请输入起始页:'))
        end = int(input('请输入终止页:'))
        params = parse.quote(name)
        for page in range(start,end+1):
            pn = (page-1)*50
            url = self.url.format(params,pn)
            self.parse_html(url)

if __name__ == '__main__':
    spider = TiebaImageSpider()
    spider.run()





















