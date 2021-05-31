import time
import random
print(str(int(time.time()*1000)))
# 1582423055202
# 1582424220679
# 158242322399
# 158242329269
# 1582423362595
# 1582423344446
# 1582423254135.1
# 1582423099991.131
# 1582423047.428883

print(random.randint(1,2))

from hashlib import md5

s = md5()
s.update(b'qifumin')
print(s.hexdigest())

print('SSS'.lower())