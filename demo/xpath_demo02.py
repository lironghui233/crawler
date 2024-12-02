
xml = """
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>Title</title>
</head>
<body>
    <ul>
        <li><a href="http://www.baidu.com">百度</a></li>
        <li><a href="http://www.google.com">谷歌</a></li>
        <li><a href="http://www.sogou.com">搜狗</a></li>
    </ul>
    <ol>
        <li><a href="feiji">飞机</a></li>
        <li><a href="dapao">大炮</a></li>
        <li><a href="huoche">火车</a></li>
    </ol>
    <div class="job">李嘉诚</div>
    <div class="common">胡辣汤</div>
</body>
</html>
"""

#xpath解析
from lxml import etree

# 加载xml内容
tree = etree.parse("D:/project/python/cap/1.html") 
result = tree.xpath("/html/body/ul/li[1]/a/text()") # xpath的顺序是从1开始数的，[]表示索引
result = tree.xpath("/html/body/ol/li/a[@href='dapao']/text()") # @表示指定的属性
# print(result)

ol_li_list = tree.xpath("/html/body/ol/li") #
for li in ol_li_list: 
    # 从每个li中提取到文字信息
    result = li.xpath("./a/text()") # 在li中继续去寻找  .相对查找
    print(result)
    result2 = li.xpath("./a/@href") # 拿到属性值：@
    print(result2)

print(tree.xpath("/html/body/ul/li/a/@href"))
print(tree.xpath("/html/body/div[1]"))