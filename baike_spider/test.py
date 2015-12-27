#!/usr/bin/env python
#encoding:utf8
#author: zeping lai

import urllib2

# 创建 Request对象
request = urllib2.Request('http://www.linuxhub.cn/test.html')

# 添加http的header
request.add_header('User-Agent','Mozilla/85.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36')

# 发送请求获取结果
response = urllib2.urlopen(request)

# 状态码
print response.getcode()

# 内容
print response.read()