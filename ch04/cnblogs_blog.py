#coding:utf-8
import re
from bs4 import BeautifulSoup
from collections import  OrderedDict
import requests
import re
# <div id="cnblogs_post_body" class="blogpost-body">
# <p>1、urlopen()方法</p>


# <a id="cb_post_title_url" class="postTitle2"
# href="http://www.cnblogs.com/themost/p/6748892.html">urlopen()&amp;urlretrieve()</a>



class HtmlOutPuter(object):
    ''' html 输出 '''
    def __init__(self):
        self.datas = []
    def collect_data(self,data):
        if data is None:
            return
        else:
            self.datas.append(data)
    def output_html(self):
        with open("output.html",'w') as fout:
            fout.write("<html>")

            fout.write('<title>Python爬虫开发与项目实战</title>')
            fout.write('<meta charset="UTF-8">')
            fout.write("<body>")
            fout.write("<table align='center' border=1 rules='all' cellpadding='15'>")
            fout.write("<tr bgcolor='# ccc'>")
            fout.write("<th> 标题 </th>")
            fout.write("<th> 链接 </th>")
            fout.write("<th> 概要 </th>")
            fout.write("</tr>")
            for data in self.datas:
                fout.write("<tr align='center'>")
                fout.write("<td>%s</td>" % data['title'].encode("utf-8"))
                # <a id="CategoryEntryList1_EntryStoryList_ctl00_Entries_TitleUrl_142" class="entrylistItemTitle" href="http://www.cnblogs.com/themost/p/6358762.html">python小知识点</a>
                fout.write('<td> <a href="%s"> %s </a></td>' % (data['url'],data['url']))
                fout.write("<td>%s</td>" % data['summary'].encode("utf-8"))
                fout.write("</tr>")
            fout.write("</table>")
            fout.write("</body>")
            fout.write("</html>")



def extract_blog(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')  # html.parser
    blog_info = OrderedDict()
    title = soup.find(id="cb_post_title_url")
    blog_info['title'] = title.string
    title_href = title.attrs['href']
    blog_info['url'] = title_href
    text = ""
    for body in soup.find_all(id="cnblogs_post_body"):
        for line in body.find_all('p'):
            if line is not None:
                text += line.string + "\n"
    blog_info['context'] = text
    return blog_info

def print_blog(blog):
    for key, value in blog.items():
        print key, ":"
        print value
        print "\n"


# nblog_1 = extract_blog('http://www.cnblogs.com/themost/p/6748892.html')
# print_blog(blog_1)
#
# blog_2 = extract_blog('http://www.cnblogs.com/themost/p/6751724.html')
# print_blog(blog_2)

outputer = HtmlOutPuter()

def extract_category(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')  # html.parser



    for item in soup.find_all(class_='entrylistItem'):
        data = {}
        title = item.find(class_='entrylistPosttitle')
        if title is not None:
            title_name = title.a.string
            url = title.a.get('href')
            print title_name
            print url
            data['title'] = title_name
            data['url'] = url
        else:
            print "title====None"
            data['title'] = ''
            data['url'] = ''
        summary = item.find(class_='entrylistPostSummary')
        if summary is not None:
            desc = summary.find(class_='c_b_p_desc')
            if desc is not None:
                text = desc.text
                print text
                # text = re.sub(r"摘要: (?P<name>\w+)阅读全文", "\g<name>", text)
                # print text
                data['summary'] = text
            else:
                print "desc====None"
                data['summary'] = ''
        else:
            print "summary====None"
            data['summary'] = ''
        print "\n"
        outputer.collect_data(data)




extract_category('http://www.cnblogs.com/themost/category/942054.html')

outputer.output_html()

# <div class="entrylistItem">
# 				<div class="entrylistPosttitle"><a id="CategoryEntryList1_EntryStoryList_ctl00_Entries_TitleUrl_1" class="entrylistItemTitle" href="http://www.cnblogs.com/themost/p/7484308.html">url的解码方式</a></div>
# 				<div class="entrylistPostSummary"><div class="c_b_p_desc">摘要: #coding:utf-8 import urllib legal_person_string = "%E6%B3%95%E5%AE%9A%E4%BB%A3%E8%A1%A8%E4%BA%BA" legal_person_string = legal_person_string.decode("gbk").encode('utf-8') legal_person_caption = urllib...<a href="http://www.cnblogs.com/themost/p/7484308.html" class="c_b_p_desc_readmore">阅读全文</a></div></div>
# 				<div class="entrylistItemPostDesc">posted @ <a href="http://www.cnblogs.com/themost/p/7484308.html" title="permalink">2017-09-06 13:14</a> 道高一尺 阅读(14) | <a href="http://www.cnblogs.com/themost/p/7484308.html#FeedBack" title="comments, pingbacks, trackbacks">评论 (0)</a>  <a href="https://i.cnblogs.com/EditPosts.aspx?postid=7484308" rel="nofollow">编辑</a></div>
# 			</div>




