# 创建 tasks.py 文件

from celery import Celery

# 初始化celery, 指定broker
app = Celery('guoxiaonao', broker='redis://:@127.0.0.1:6379/6')

# 创建任务函数
@app.task
def task_test():
    print("task is running....")
