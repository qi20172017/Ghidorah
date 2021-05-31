"""
腾讯招聘指定类别的职位信息抓取 - 多线程
"""
import requests
import json
from threading import Thread,Lock
from queue import Queue
from fake_useragent import UserAgent
import time
from urllib import parse

class TencentSpider:
    def __init__(self):
        self.one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1563912271089&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
        self.two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1563912374645&postId={}&language=zh-cn'
        # 两个队列,分别存放两级页面的URL地址
        self.one_q = Queue()
        self.two_q = Queue()
        # 锁
        self.lock1 = Lock()
        self.lock2 = Lock()
        # 计数
        self.i = 0

    def get_html(self,url):
        """请求功能函数"""
        headers = { 'User-Agent':UserAgent().random }
        html = requests.get(url=url,headers=headers).text
        return html

    def url_in(self):
        """URL地址入队列"""
        word = input('请输入职位类别:')
        word = parse.quote(word)
        # 想办法获取这个类别的总页数
        total = self.get_total(word)
        for page in range(1,total+1):
            url = self.one_url.format(word,page)
            self.one_q.put(url)

    def get_total(self,word):
        """获取word类别的总页数"""
        url = self.one_url.format(word,1)
        html = json.loads(self.get_html(url=url))
        count = html['Data']['Count']
        # 20个职位 : 2页 count//10
        # 25个职位 : 3页 count//10 + 1
        total = count//10 if count%10==0 else count//10 + 1
        return total

    def parse_one_page(self):
        """线程1事件函数 - 获取所有职位的postId的值"""
        while True:
            self.lock1.acquire()
            if not self.one_q.empty():
                one_url = self.one_q.get()
                self.lock1.release()
                # 请求获取html,解析提取 postId 的值
                html = json.loads(self.get_html(url=one_url))
                for one_job in html['Data']['Posts']:
                    post_id = one_job['PostId']
                    # 拼接二级页面URL地址,入队列self.two_q
                    two_url = self.two_url.format(post_id)
                    # 加锁和释放锁
                    self.lock1.acquire()
                    self.two_q.put(two_url)
                    self.lock1.release()
            else:
                self.lock1.release()
                break

    def parse_two_page(self):
        """线程2的事件函数 - 获取具体的职位信息"""
        while True:
            try:
                self.lock2.acquire()
                two_url = self.two_q.get(block=True,timeout=3)
                self.lock2.release()
                # 请求 + 解析
                html = json.loads(self.get_html(url=two_url))
                item = {}
                item['name'] = html['Data']['RecruitPostName']
                item['address'] = html['Data']['LocationName']
                item['type'] = html['Data']['CategoryName']
                item['time'] = html['Data']['LastUpdateTime']
                item['duty'] = html['Data']['Responsibility']
                item['require'] = html['Data']['Requirement']
                print(item)
                # 计数
                self.lock2.acquire()
                self.i += 1
                self.lock2.release()
            except Exception as e:
                # 一旦捕捉到异常,说明try中上锁成功,但是未释放锁
                self.lock2.release()
                print(e)
                break

    def run(self):
        # URL地址入队列
        self.url_in()
        t1_list = []
        t2_list = []
        # 线程1 - 一级页面
        for i in range(2):
            t1 = Thread(target=self.parse_one_page)
            t1_list.append(t1)
            t1.start()

        # 线程2 - 二级页面
        for i in range(2):
            t2 = Thread(target=self.parse_two_page)
            t2_list.append(t2)
            t2.start()

        for t in t1_list:
            t.join()

        for t in t2_list:
            t.join()

        print('职位数量:',self.i)

if __name__ == '__main__':
    start_time = time.time()
    spider = TencentSpider()
    spider.run()
    end_time = time.time()
    print('时间:%.2f' % (end_time-start_time))










