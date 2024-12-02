
# xpath 是在XML文档中搜索内容的一门语言
# html 是XML的一个子集

# 安装lxml模块  pip install lxml

xml = """
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大枪</nick>
        <nick id="10010">周芷若</nick>
        <nick id="jay">周杰伦</nick>
        <div>
            <nick>惹了</nick>
        </div>
        <span>
            <nick>热啊冷啊温度合适</nick>
            <div>
                <nick>惹了22</nick>
            </div>
        </span>
    </author>

    <partner>
        <nick id="ppc">胖胖陈</nick>
        <nick id="ppbc">胖胖不陈</nick>
    </partner>
</book>
"""

#xpath解析
from lxml import etree

# 加载xml内容
tree = etree.XML(xml)
# 解析内容
result = tree.xpath("/book") # /表示层级关系，第一个/是根节点
print(result)
result = tree.xpath("/book/name")
print(result)
result = tree.xpath("/book/name/text()") # text()拿文本
print(result)
result = tree.xpath("/book/author/nick/text()") # text()拿文本
print(result)
result = tree.xpath("/book/author/div/nick/text()") # text()拿文本
print(result)
result = tree.xpath("/book/author//nick/text()") # 拿所有author下nick（包括子和孙）
print(result)
result = tree.xpath("/book/author/*/nick/text()") # 拿所有author/*/下nick
print(result)