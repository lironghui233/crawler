

import re

# # findall： 匹配字符串中所有的符合正则的内容
# lst = re.findall("\d+","我的电话号码是:10086，我女朋友的电话时：10010")
# print(lst)

# # finditer： 匹配字符串中所有的内容【返回的是迭代器】，从迭代器中拿到内容需要.group()
# it = re.finditer("\d+","我的电话号码是:10086，我女朋友的电话时：10010")
# print(it)
# for i in it:
#     print(i.group())


# # search，找到一个结果就返回，返回的结果是match对象。 拿数据需要.group() 
# s = re.search(r"\d+","我的电话号码是:10086，我女朋友的电话时：10010")
# print(s.group())


# match是从头开始匹配
# s = re.match(r"\d+","我的电话号码是:10086，我女朋友的电话时：10010")
# print(s.group())


# #预加载正则表达式
# obj = re.compile(r"\d+")

# ret = obj.findall("我的电话号码是:10086，我女朋友的电话时：10010")
# print(ret)

# ret = obj.finditer("我的电话号码是:10086，我女朋友的电话时：10010")
# for it in ret:
#     print(it.group())


s = """
<div class='jay'><span id='1'>牛逼</span></div>
<div class='jj'><span id='2'>天才</span></div>
<div class='jolin'><span id='3'>健康</span></div>
<div class='sylar'><span id='4'>长寿</span></div>
<div class='tory'><span id='5'>幸运</span></div>
"""

# (?P<分组名字>正则)：  可以单独从正则匹配的内容中进一步提取内容
obj = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<wahaha>.*?)</span></div>", re.S) # re.S: 让.能匹配换行符

result = obj.finditer(s)
for it in result:
    print(it.group("wahaha"))
    print(it.group("id"))