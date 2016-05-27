
#!/usr/bin/env python
#encoding:utf8
#author: zeping lia

import sys
import httplib

def get_headers_info(url):
    '''
    获取url的http头信息
    :param url:
    :return:
    '''

    conn = httplib.HTTPSConnection(url)
    conn.request("HEAD","/")
    res = conn.getresponse()
    headers =  res.getheaders()
    return headers


if __name__ == "__main__":

    try:
        url = sys.argv[1]
        # url = "http://www.linuxhub.cn"
        headers = get_headers_info(url)
        print ""
        for head in headers:
            print head[0] + ": " + head[1]
        print ""

    except:
        print "\n请在脚本后面输入url地址!  "
        print "例: %s http://www.linuxhub.org\n" % sys.argv[0]
