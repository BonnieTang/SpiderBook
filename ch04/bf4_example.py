#coding:utf-8
import bs4
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
#print soup.prettify()

# tag有两个重要的属性，name和attributes
print soup.name  # [document]  soup比较特殊
print soup.title.name # title

# tag还可以修改name
soup.title.name = 'mytitle'
print soup.title  # None
print soup.mytitle  #<mytitle>The Dormouse's story</mytitle>
# 再修改回去
soup.mytitle.name = 'title'

# tag的属性操作方法与字典相同
print soup.p['class']  # ['title']
print soup.p.get('class') # ['title']

#  也可以直接取所有的属性
print soup.p.attrs  # {'class': ['title']}
# 也可以进行修改
soup.p['class']="myClass"
print soup.p # <p class="myClass"><b>The Dormouse's story</b></p>


## NavigableString类型
print soup.p.string # The Dormouse's story
print type(soup.p.string) # <class 'bs4.element.NavigableString'>
## NavigableString类型 可以直接转码
unicode_string = unicode(soup.p.string)
print unicode_string # The Dormouse's story
print type(unicode_string) # <type 'unicode'>

print type(soup.name)  # <type 'unicode'>
print soup.name
print soup.attrs

# a标记对内容部分实际上是注释，所以先判断一下类型，再进行字符串提取处理
print soup.a.string
print type(soup.a.string)
if type(soup.a.string)==bs4.element.Comment:
    print soup.a.string

# 将tag子节点以列表形式进行输出
print soup.head.contents  # [<title>The Dormouse's story</title>]
print len(soup.head.contents) # 1
print soup.head.contents[0].string  # The Dormouse's story

# 返回的是生成器，对tag对子节点进行循环
for child in soup.head.children:
    print(child)
    # <title>The Dormouse's story</title>

# 子孙节点 递归循环遍历打印
for child in soup.head.descendants:
    print(child)
    # <title>The Dormouse's story</title>
    #The Dormouse's story

# 如果一个标记里面没有标记了，那么string返回标记里面的内容
# 如果标记里面只有唯一的标记了，那么string也会返回最里面的内容
# 如果tag包含了多个子节点，tag就无法确定，该调用那一个，于是就输出None
print soup.head.string # The Dormouse's story
print soup.title.string # The Dormouse's story
print soup.html.string # None

# 应用于tag中包含多个字符串的情况，可以进行循环遍历
for string in soup.strings:
    print(repr(string))

# 去掉输出字符串中包含的空格或空行
for string in soup.stripped_strings:
    print(repr(string))

# 获取元素的父节点
print soup.title  # <title>The Dormouse's story</title>
print soup.title.parent # <head><title>The Dormouse's story</title></head>


print soup.a  # <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

# 兄弟节点
print soup.p.next_sibling
print soup.p.prev_sibling
print soup.p.next_sibling.next_sibling

# 兄弟节点迭代输出
for sibling in soup.a.next_siblings:
    print(repr(sibling))

# 前后节点，不分层次
print soup.head
print soup.head.next_element

# 迭代器，前后节点
for element in soup.a.next_elements:
    print(repr(element))


