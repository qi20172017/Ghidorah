import pymysql
db = pymysql.connect('127.0.0.1','root','123456','maoyandb',charset = 'utf8')
cursor = db.cursor()

sql = 'insert into maoyantab values(%s,%s,%s)'
data = [['a','rrrr','123'],['d','rrrr','123'],['c','rrrr','123'],['b','rrrr','123']]
cursor.executemany(sql,data)
db.commit()
cursor.close()
db.close()