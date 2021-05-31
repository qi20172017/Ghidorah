import re

html = """
<div class="animal">
    <p class="name">
		<a title="Tiger"></a>
    </p>
    <p class="content">
		Two tigers two tigers run fast
    </p>
</div>

<div class="animal">
    <p class="name">
		<a title="Rabbit"></a>
    </p>

    <p class="content">
		Small white rabbit white and white
    </p>
</div>
"""
pattern = re.compile('<a title="(.*?)">.*?"content">\s+(.*?)\s+</p>',re.S)
res = pattern.findall(html)
print(res)
for item in res:
    print('动物名称：%s\n动物描述：%s'%item)
    print('*'*40)