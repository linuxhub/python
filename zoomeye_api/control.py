#!/usr/bin/env python
#encoding:utf8
#author: zeping lai

#def request1(appkey, m="GET"):

import json
import urllib2

class Zoomeye(object):

        def __init__(self):
            self.base_url = "https://api.zoomeye.org"
            self.username = ""
            self.password = ""
            self.access_token = ""

        def request(self, m="GET", path=""):
            url = "%s%s" %(self.base_url, path)
            print url
            if m == "GET":
                authorization = "JWT %s" % self.access_token
                headers = {'Content-Type': 'application/json'}
                headers["Authorization"] = authorization
                req = urllib2.Request(url=url,headers=headers)
            else:
                headers = {'Content-Type': 'application/json'}
                params = {'username': self.username , 'password': self.password}
                data = json.dumps(params)
                req = urllib2.Request(url, data, headers)
            try:
                f = urllib2.urlopen(req)
                response = f.read()
                f.close()
                res = json.loads(response)
                return res
            except:
                return None

        def login(self):
            path = "/user/login"
            res = self.request(m="POST", path=path)
            access_token = res['access_token']
            self.access_token = access_token
            return access_token

        def dv_gz(self,page=1):
            bash_path = "/host/search?query=DVRDVS-WEBs+country%3AChina+city%3AGuangzhou+&t=host"
            path = bash_path + "&page=%s" % page
            res = self.request(m="GET", path=path)
            if res is None:
                return None
            else:
                return res

