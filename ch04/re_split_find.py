#coding:utf-8
import re

# 将正则表达式编译成pattern对象
pattern = re.compile(r'\d+')

# re.split(pattern, string[, maxsplit])
# 按照能够匹配的子串进行分割, maxsplit用于制定最大分割次数，不指定则全部分割
print re.split(pattern,'A1B2C3D4')
# ['A', 'B', 'C', 'D', '']
print re.split(pattern,'A1B2C3D4',2)
# ['A', 'B', 'C3D4']

# re.findall (pattern, string[, flags])
# 搜索整个串，以列表形式返回能匹配的全部子串
print re.findall(pattern,'A1B2C3D4')
# ['1', '2', '3', '4']

# re.finditer (pattern, string[, flags])
# 迭代器形式返回能匹配的全部match对象
matchiter = re.finditer(pattern,'A1B2C3D4')
for match in matchiter:
    print match.group()
#    1
#    2
#    3
#    4

