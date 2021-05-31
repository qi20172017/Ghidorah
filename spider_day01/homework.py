import random
from urllib import request,parse
import re
import time
import pymysql
import csv
class Maoyan_spider():
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = ['Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
                        # 'User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                        # 'User-Agent:Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                        # 'User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
                        # 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        ]
        self.db = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',database='maoyandb',charset='utf8')
        self.cur = self.db.cursor()

        # self.cookie = '__mta=145185035.1582019849375.1582022236956.1582026322825.6; uuid_n_v=v1; uuid=51C60E20523511EAAF9C3170808A716906C02763B4E542E898132A4EBDEE5A17; _csrf=7c6eadaf2fb7cb74a17bc814afc54894a2fa2eb4768f22bb0cc8d822c4d8461b; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1582019836,1582075301,1582075475; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1582075475; _lxsdk_cuid=17057bafb28c8-028177f99c8243-71206751-100200-17057bafb29c8; _lxsdk=51C60E20523511EAAF9C3170808A716906C02763B4E542E898132A4EBDEE5A17; mojo-uuid=518095f996df8debcce818b618d277c3; _lxsdk_s=1705b072274-677-048-53e%7C%7C9; mojo-trace-id=5; mojo-session-id={"id":"7bd0547b5a843d11709b116bfcc625ad","time":1582075300937}; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __mta=145185035.1582019849375.1582026322825.1582075483177.7; lt=W7baauD-uQbxSqcRC7OUgJfYJIEAAAAAEQoAAPOPRClFTfCVVhhx-OzArBpKW4-pQm1D_9ZRp6MDucFjzgCyJgUtp1us2nrMgP-Y0A; lt.sig=VKP61FR2T0O2Ry932wsst_BTy1E'
    def get_html(self,page):
        full_url = self.url.format((page-1)*10)
        req = request.Request(url=full_url,headers={'User-Agent':random.choice(self.headers)})
        res = request.urlopen(req)
        return res.read().decode()

    def parse_html(self,html):
        pattern = re.compile('<dd>.*?title="(.*?)".*?主演：(.*?)\s.*?上映时间：(.*?)</p.*?</dd>', re.S)
        res = pattern.findall(html)
        print(res)
        return res


    def save_html(self,html,page):

        file_name = str(page) + '.html'
        with open(file_name,'w') as f:
            f.write(html)

    def save_csv(self,info):
        with open('move.csv','a+')as f:
            write_csv = csv.writer(f)
            write_csv.writerows(info)

    def save_info(self,info):

        sql = "insert into maoyantab values (%s,%s,%s)"
        self.cur.executemany(sql,info)
        self.db.commit()

    def run(self):
        start_page = int(input('输入起始页：'))
        end_page = int(input('输入终止页:'))
        for i in range(start_page,end_page+1):
            html = self.get_html(i)
            res = self.parse_html(html)
            if not res:
                # self.save_html(html,i)
                print('下载第{}页失败！'.format(i))
            else:
                # self.save_info(res)
                self.save_csv(res)
                print('下载第{}页完成！'.format(i))
            sleeptime = random.randrange(4,10)
            for i in range(sleeptime):
                print(i)
                time.sleep(1)
        self.cur.close()
        self.db.close()


if __name__ == '__main__':
    myspider = Maoyan_spider()
    myspider.run()
