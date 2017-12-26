#coding:utf-8
import re
from bs4 import BeautifulSoup
html_str = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2"><!-- Lacie --></a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html_str,'lxml', from_encoding='utf-8')

# 字符串参数，查找<b>
print soup.find_all('b')
# 正则表达式入参
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)

# 传入参数列表
print soup.find_all(["a", "b"])

# 可以匹配任何值，找到所有的tag，但是不会返回字符串节点
for tag in soup.find_all(True):
    print(tag.name)

# 传递方法，过滤包含class属性，也包含id属性的元素
def hasClass_Id(tag):
    return tag.has_attr('class') and tag.has_attr('id')
print soup.find_all(hasClass_Id)

# 当作属性名来搜索
print soup.find_all(id='link2')  # [<a class="sister" href="http://example.com/lacie" id="link2"><!-- Lacie --></a>]

print soup.find_all(href=re.compile("elsie"))  # [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]

# 包含id的属性
print soup.find_all(id=True)

# 用class过滤，因为是关键字，要加一个下划线
print soup.find_all("a", class_="sister")

# 多个tag属性，一起过滤
print soup.find_all(href=re.compile("elsie"), id='link1')



#data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
# data_soup.find_all(attrs={"data-foo": "value"})

print "-----------------------------------"
print soup.find_all(text="Elsie")  ## <!-- Elsie --> 查询为空，取消注释，且去空才可以
print soup.find_all(text=["Tillie", "Elsie", "Lacie"])
print soup.find_all(text=re.compile("Dormouse"))

print soup.find_all("a", text="Elsie")


# 限制出差数量
print soup.find_all("a", limit=2)

# recursive=False 表示只想搜索tag的直接子节点
print soup.find_all("title")
print soup.find_all("title", recursive=False)
