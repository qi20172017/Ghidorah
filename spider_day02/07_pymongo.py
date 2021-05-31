import pymongo

conn = pymongo.MongoClient(host='localhost',port=27017)
db = conn['maoyandb']
myset = db['maoyanset']
myset.insert_one({'name':'速度与激情','time':'2000'})
print('ok')