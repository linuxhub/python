#!/usr/bin/env python
#encoding:utf8
#author: zeping lai

import sys
import httplib2

def get_http_resp_headers(url):
    h = httplib2.Http(".cache")
    resp_headers, content = h.request(url, "GET")
    return resp_headers

if __name__ == "__main__":

    try:
        url = sys.argv[1]
        # url = "http://www.linuxhub.cn"
        resp_headers = get_http_resp_headers(url)
        print ""
        print "URL: " + url
        for d, x in resp_headers.items():
            print d + ": " + x
        print ""
        
    except:
        print "\n请在脚本后面输入url地址!  "
        print "例: %s http://www.linuxhub.org\n" % sys.argv[0]
