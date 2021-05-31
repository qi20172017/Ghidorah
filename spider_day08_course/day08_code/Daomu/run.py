# import os
#
# print(os.path.exists('./a'))
# # os.makedirs('./a/b')
# os.mkdir('./a')
# print(os.path.exists('./a'))
from scrapy import cmdline
cmdline.execute('scrapy crawl daomu2'.split())
