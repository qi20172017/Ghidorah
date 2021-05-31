"""
csv模块使用
"""
import csv

# 1. writerow(): 一次只能写入1行
with open('风云.csv','w') as f:
    # 1.初始化写入对象
    # 2.写入数据
    writer = csv.writer(f)
    writer.writerow(['聂风','雪饮狂刀'])

# 2.writerows():一次性写入多行
with open('风云.csv','w') as f:
    writer = csv.writer(f)
    writer.writerows([('步惊云','绝世好剑'),('秦霜','天霜拳')])


















