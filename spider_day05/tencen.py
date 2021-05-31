import random
import json
import requests
import time
from fake_useragent import UserAgent
from threading import Thread
from queue import Queue
class TencenSpider(object):
    def __init__(self):
        self.page_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1582542878722&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
        self.info_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp={}&postId={}&language=zh-cn'
        self.q = Queue()

    def get_html(self,url):
        headers = {
            'User-Agent':UserAgent().random
        }
        html = requests.get(url=url,headers=headers).json()
        return html


    def save_html(self,html):
        with open('info.html','w')as f:
            f.write(html)

    def get_id(self):
        for i in range(1,453):
            page_url = self.page_url.format(1)
            page_html = self.get_html(url=page_url)
            for i in page_html['Data']['Posts']:
                self.q.put(i['PostId'])

    def job_info(self):
        count = 0
        while True:
            info_dict = {}
            try:
                job_id = self.q.get(timeout=15)
            except Exception as e:
                print(e)
                print(count)
                break
            timestamp = int(time.time() * 1000)
            url = self.info_url.format(timestamp, job_id)

            info_html = self.get_html(url=url)
            info_dict['职位名称'] = info_html['Data']['RecruitPostName']
            info_dict['职位地址'] = info_html['Data']['LocationName']
            info_dict['职位类别'] = info_html['Data']['CategoryName']
            info_dict['发布时间'] = info_html['Data']['LastUpdateTime']
            info_dict['工作职责'] = info_html['Data']['Responsibility']
            info_dict['工作要求'] = info_html['Data']['Requirement']
            print(info_dict)
            count+=1
        # time.sleep(random.uniform(1, 3))

    def run(self):
        t_liat = []
        t1 = Thread(target=self.get_id)
        t_liat.append(t1)
        t1.start()

        for i in range(5):
            t = Thread(target=self.job_info)
            t_liat.append(t)
            t.start()

        for t in t_liat:
            t.join()



if __name__ == '__main__':
    myspider = TencenSpider()
    myspider.run()

    # 1582544697685
    # 1582545310291

    # http: // careers.tencent.com / jobdesc.html?postId = 0
    # https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1582544697685&postId=1216304000593301504&language=zh-cn
    # http: // careers.tencent.com / jobdesc.html?postId = 1216304000593301504
    # http: // careers.tencent.com / jobdesc.html?postId = 1211973021942681600
    # http: // careers.tencent.com / jobdesc.html?postId = 1231242172360036352
    # http: // careers.tencent.com / jobdesc.html?postId = 1231242184901005312
    # http: // careers.tencent.com / jobdesc.html?postId = 1231242239208853504
    # http: // careers.tencent.com / jobdesc.html?postId = 1231242253146525696
    # http: // careers.tencent.com / jobdesc.html?postId = 1231242271291084800
    # http: // careers.tencent.com / jobdesc.html?postId = 1231771979799859200
    # http: // careers.tencent.com / jobdesc.html?postId = 1231772173006278656


    # 1231896040609681408
    # 1216304000593301504
    # 1211973021942681600
    # 1231242172360036352
    # 1231242184901005312
    # 1231242239208853504
    # 1231242253146525696
    # 1231242271291084800
    # 1231771979799859200
    # 1231772173006278656

    # https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1582543425732&postId=1231851771693895680&language=zh-cn