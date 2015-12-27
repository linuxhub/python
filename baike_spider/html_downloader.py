#!/usr/bin/env python
#encoding:utf8
#author: zeping lai


# 3. HTML下载器

import urllib2

class HtmlDownloader(object):

    def download(self,url):
        '''
        下载url内容
        :param url: url地址
        :return:  返回下载好的内容
        '''

        if url is None:
            return None

        response = urllib2.urlopen(url)

        # 请求返回的状态不等于200,请求失败返回 None
        if response.getcode() != 200:
            return None

        return response.read()