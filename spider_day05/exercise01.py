import json
# dict01 = {
#     'name':'qifumin'
# }
# j_dict01 = json.dumps(dict01)
# a_dict01 = json.loads(j_dict01)
# print(a_dict01)
import random
from threading import Thread
from queue import Queue
import time

q = Queue()
def fuc01():
    for i in range(5):
        time.sleep(1)
        q.put(random.randint(1,5))
        num = random.randint(1,5)
        print('fuc01:{}'.format(num))


def fuc02():

    while True:
        print('fuc02>>>>>{}'.format(q.get(block=True,timeout=8)))

t1 = Thread(target=fuc01)

t1.start()

fuc02()
t1.join()
# https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=金毛&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=金毛&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=240&rn=30&gsm=f0&1582551880766=