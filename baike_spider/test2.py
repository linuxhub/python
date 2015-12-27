#!/usr/bin/env python
#encoding:utf8
#author: zeping lai

#http://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(
                    html_doc,             # HTML文档字符串
                    'html.parser',        # HTML解析器
                    from_encoding='utf-8' # HTML文档解析器
                    )


print "获取所有的链接"
links = soup.find_all('a')
n = 1
for link in links:
    print n, link['href'],link.get_text()
    n = n+1

print "获取lacie的链接"
link_node = soup.find('a', href='http://example.com/lacie')
print link_node['href'],link_node.get_text()


print "正则匹配"
import re
link_node = soup.find('a', href=re.compile(r"ill"))
print link_node['href'],link_node.get_text()


print "获取p段落内容"
p_node = soup.find('p', class_="title") #class是python的关键字,加个下划线
print p_node.get_text()
