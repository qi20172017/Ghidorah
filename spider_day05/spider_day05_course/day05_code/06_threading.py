"""
多线程示例
"""
from threading import Thread

# 线程1事件函数
def f1():
    print('我是f1')


t_list = []

for i in range(5):
    t = Thread(target=f1)
    t_list.append(t)
    t.start()

for m in t_list:
    m.join()



















