import csv

with open('aa.csv','w') as f:
    write_csv = csv.writer(f)
    write_csv.writerows([('aaa','bbb','ccc'),('eee','rrr','ttt')])