import pymysql

db = pymysql.connect(host='127.0.0.1',port=3306,database='maoyandb',user='root',password='123456',charset='utf8')
cur = db.cursor()
sql = 'insert into maoyantab values(%s,%s,%s)'
r_list = [('大话稀有','周星驰','1990'),('秋香','周星驰','1997')]
for i in r_list:
    cur.execute(sql,i)
db.commit()

cur.close()
db.close()