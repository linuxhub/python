#!/usr/bin/env python
#encoding:utf8
#author: zeping lai

# 1.爬虫总调度程序


from python.baike_spider import url_manager
from python.baike_spider import html_downloader
from python.baike_spider import html_parser
from python.baike_spider import html_outputer


class SpiderMain(object):

    #初始化对象
    def __init__(self):
        self.urls = url_manager.UrlManager()                #URL管理器
        self.downloader = html_downloader.HtmlDownloader()  #下载器
        self.parser = html_parser.HtmlParser()              #解析器
        self.outputer = html_outputer.HtmlOutputer()        #输出器

    def craw(self, root_url):
        count = 1 #记录当前爬取的是第几个url

        self.urls.add_new_url(root_url)

        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()                         # [2.url管理器] 获取一个等待爬取的url
                print 'craw %s : %s ' %(count, new_url)                   #打印出当前爬的是第几个及是那个URL
                html_cont = self.downloader.download(new_url)             # [3.网页下载器] 启动下载器下载页面
                new_urls,new_data = self.parser.parse(new_url, html_cont) # [4.网页解析器] 调用解析器来解析这个页面数据,得到新的url列表以及新的数据
                self.urls.add_new_urls(new_urls)                          #新的url地址补充到url管理器
                self.outputer.collect_data(new_data)                      # [5.网页输出器] 数据的收集

                # 本爬虫是爬取10个页面,到了10个break
                if count == 10:
                    break
                count = count + 1

            except:
                print "crae failed"

        self.outputer.output_html()  #来输出收集好的数据

if __name__ == '__main__':
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()  #
    obj_spider.craw(root_url)  #启动爬虫