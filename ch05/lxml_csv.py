# coding:utf-8
import csv
import re

import requests
from lxml import etree

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
r = requests.get('http://seputu.com/', headers=headers)
# 使用lxml解析网页

html = etree.HTML(r.text)
div_mulus = html.xpath('.//*[@class="mulu"]')  # 先找到所有的div class=mulu标签
pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
rows = []
for div_mulu in div_mulus:
    # 找到所有的div_h2标签
    div_h2 = div_mulu.xpath('./div[@class="mulu-title"]/center/h2/text()')
    if len(div_h2) > 0:
        h2_title = div_h2[0].encode('utf-8')
        a_s = div_mulu.xpath('./div[@class="box"]/ul/li/a')
        for a in a_s:
            # 找到href属性
            href = a.xpath('./@href')[0].encode('utf-8')
            # 找到title属性
            box_title = a.xpath('./@title')[0]
            pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
            match = pattern.search(box_title)
            if match != None:
                date = match.group(1).encode('utf-8')
                real_title = match.group(2).encode('utf-8')
                # print real_title
                content = (h2_title, real_title, href, date)
                print content
                rows.append(content)
headers = ['title', 'real_title', 'href', 'date']
with open('qiye.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

# 创建reader对象，读取内容
with open('qiye.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    print headers
    for row in f_csv:
        print row
