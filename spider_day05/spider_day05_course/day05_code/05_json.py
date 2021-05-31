"""
json模块的dump()方法
"""
import json

# item = {'name':'帝景城','price':'500万','address':'北京'}
# with open('lianjia.json','w') as f:
#     json.dump(item,f,ensure_ascii=False)

house_list = [
    {'name':'帝景城','price':'500万','address':'北京'},
    {'name':'帝景又一城','price':'600万','address':'上海'},
    {'name':'帝景又又一城','price':'700万','address':'上海'},
]
with open('lianjia.json','w') as f:
    json.dump(house_list,f,ensure_ascii=False)














