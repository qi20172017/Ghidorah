"""
线程锁
"""
from threading import Thread,Lock

n = 5000
lock = Lock()

def f1():
    global n
    for i in range(1000000):
        lock.acquire()
        n = n + 1
        lock.release()

def f2():
    global n
    for i in range(1000000):
        lock.acquire()
        n = n - 1
        lock.release()

t1 = Thread(target=f1)
t1.start()

t2 = Thread(target=f2)
t2.start()

t1.join()
t2.join()

print(n)

"""
n = 5000
正常: 1次+1 , 1次-1
x = n + 1  :x=5001
n = x      :n=5001
x = n - 1  :x=5000
n = x      :n=5000

不正常: 1次+1 , 1次-1
x = n + 1  :x=5001
x = n - 1  :x=4999
n = x      :n=4999
n = x      :n=4999
"""









