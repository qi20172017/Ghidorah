import re

html = """
<div><p>如果你为门中弟子伤她一分，我便屠你满门</p></div>
<div><p>如果你为天下人损她一分，我便杀尽天下人</p></div>
"""

pattern = re.compile('<div><p>(.*?)</p></div>',re.S)
r = pattern.findall(html)
print(r)

s='A B C D'
pattern = re.compile('\w+\s+\w+')
print(pattern.findall(s))
a = re.compile('(\w+)\s+\w+')
print(a.findall(s))

a = re.compile('(\w+)\s+(\w+)')
print(a.findall(s))