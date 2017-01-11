#!/usr/bin/env python
#encoding:utf8
#author: zeping lai

from control import Zoomeye
from process import Process
from outputer import Outputer

from model import db
from model import Host

class ZoomeyeMain(object):

    def __init__(self):
        self.zoomeye = Zoomeye()
        self.process = Process()
        self.outputer = Outputer()

    def run(self):
        self.zoomeye.username = "root@linuxhub.cn"
        self.zoomeye.password = "123456"
        self.zoomeye.base_url = "https://api.zoomeye.org"
        self.zoomeye.login()
        res = self.zoomeye.dv_gz()

        #数据库page列，最大值
        host = Host.query.order_by(Host.page.desc()).limit(1).first()
        if host:
            if host.page:
                page = host.page
            else:
                page = 0
        else:
            page = 0

        if host is None:
            page = 0
        while res:
            page = page + 1
            res = self.zoomeye.dv_gz(page=page)
            data_list = self.process.parser(res)
            self.outputer.storage(data_list,page)
            # if page == 2:
            #     res = None


zoomeye_main = ZoomeyeMain()
zoomeye_main.run()
