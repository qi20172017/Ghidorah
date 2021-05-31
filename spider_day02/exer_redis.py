# import redis
#
# r = redis.Redis(host='127.0.0.1',port=6379,db=0)
# r.sadd('name','qifumin')

from hashlib import md5
s = md5()
s1 = 'qifumin'
s.update(s1.encode())
sd = s.hexdigest()
print(sd)