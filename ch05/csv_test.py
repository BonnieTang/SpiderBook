# coding:utf-8
from collections import  namedtuple
import csv

# 写入csv文件，rows为元组列表
headers = ['ID','UserName','Password','Age','Country']
rows = [(1001,"qiye","qiye_pass",24,"China"),
         (1002,"Mary","Mary_pass",20,"USA"),
         (1003,"Jack","Jack_pass",20,"USA"),
       ]
with open('qiye.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

# 写入csv文件，rows也可以是字典数据
headers = ['ID','UserName','Password','Age','Country']
rows = [{'ID':1001,'UserName':"qiye",'Password':"qiye_pass",'Age':24,'Country':"China"},
{'ID':1002,'UserName':"Mary",'Password':"Mary_pass",'Age':20,'Country':"USA"},
{'ID':1003,'UserName':"Jack",'Password':"Jack_pass",'Age':20,'Country':"USA"},
]

with open('qiye.csv','w') as f:
    f_csv = csv.DictWriter(f,headers)
    f_csv.writeheader()
    f_csv.writerows(rows)

# 创建reader对象，读取内容
with open('qiye.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    print headers
    for row in f_csv:
        print row

# 使用命名元组
with open('qiye.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    Row = namedtuple('Row',headers)
    for r in f_csv:
        row = Row(*r)
        print row.UserName,row.Password
        print row

# 读取到字典序列

with open('qiye.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print row.get('UserName'), row.get('Password')