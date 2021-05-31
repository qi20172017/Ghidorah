"""
使用executemany()方法一次性插入多条表记录
"""
import pymysql

db = pymysql.connect('127.0.0.1','root','123456','maoyandb',charset='utf8')
cursor = db.cursor()
ins = 'insert into maoyantab values(%s,%s,%s)'
r_list = [
    ('大话西游之月光宝盒','周星驰','1993'),
    ('大话西游之大圣娶亲','周星驰','1994')
]
cursor.executemany(ins,r_list)
db.commit()
cursor.close()
db.close()
print('ok')





















