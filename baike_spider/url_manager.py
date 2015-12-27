#!/usr/bin/env python
#encoding:utf8
#author: zeping lai

# 2.URL管理器


class UrlManager(object):

    def __init__(self):
        # URL管理器需要维护两个列表,
        # 第一个等爬取的URL列表, 第三个是爬取过的URL列表
        self.new_urls = set()  # 待爬取的url列表
        self.old_urls = set()  # 爬取过的ur列表

    def add_new_url(self,url):
        '''
        向管理器中添加一个URL
        :param url: 单个url地址
        :return:
        '''

        if url is None:
            return

        # 既不在待爬取的列表里面,也不在爬取过的url列表里面, 说明一个弹性的url可以用来行爬取
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)


    def add_new_urls(self,urls):
        '''
        向管理器添加批量的URL
        :param urls: 批量的urls列表
        :return:
        '''
        if urls is None or len(urls) == 0:
            return

        for url in urls:
            self.add_new_url(url) #进行单个的添加


    def has_new_url(self):
        '''
        判断管理器是否有新的待爬取的URL
        :return:
        '''

        # 如果urls的长度不为次的话,那就说明的待爬取的url
        return len(self.new_urls) != 0


    def get_new_url(self):
        '''
        从URL管理器中获取一个新的待爬取的URL
        :return:  返回一个爬取的URL
        '''

        new_url = self.new_urls.pop()  # pop这个方法会在列表中获取一个url,并且会移除这个url
        self.old_urls.add(new_url)     # 添加到爬取过的ur列表
        return new_url

