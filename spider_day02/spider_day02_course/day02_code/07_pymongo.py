"""
库: maoyandb
集合: maoyanset
在maoyanset中插入1条文档: {'name':'速度与激情','time':'2000'}
"""
# sudo pip3 install pymongo
import pymongo

# 1.连接数据库
conn = pymongo.MongoClient('localhost',27017)
# 2.创建库对象
db = conn['maoyandb']
# 3.创建集合对象
myset = db['maoyanset']
# 4.插入文档
myset.insert_one({'name':'速度与激情','time':'2000'})
print('ok')









