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


#直接查找title标签
print soup.select("title")
#逐层查找title标签
print soup.select("html head title")
#查找直接子节点
#查找head下的title标签
print soup.select("head > title")
#查找p下的id="link1"的标签
print soup.select("p > #link1")
# [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]


#查找兄弟节点
#查找id="link1"之后class=sisiter的所有兄弟标签
print soup.select("#link1 ~ .sister")
# [<a class="sister" href="http://example.com/lacie" id="link2"><!-- Lacie --></a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

#查找紧跟着id="link1"之后class=sisiter的子标签
print soup.select("#link1 + .sister")
# [<a class="sister" href="http://example.com/lacie" id="link2"><!-- Lacie --></a>]


## 通过类名查找
print soup.select(".sister")
print soup.select("[class~=sister]")

