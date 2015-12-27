#!/usr/bin/env python
#encoding:utf8
#author: zeping lai

# 4.HTML解析器

from bs4 import BeautifulSoup
import re
import urlparse


class HtmlParser(object):


        def _get_new_urls(self, page_url, soup):
            '''
             获取url列表,匹配出页面所有词条的url
            :param page_url:
            :param soup:
            :return:
            '''

            new_urls = set()

            # 需要匹配的内容格式  Url/view/123.html
            links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))  #获取所有的链接

            for link in links:
                new_url = link['href']
                new_full_url = urlparse.urljoin(page_url, new_url)  #拼接url
                new_urls.add(new_full_url)
            return new_urls



        def _get_new_data(self, page_url, soup):
            '''
            获取数据,解析出了titel与summary两个数据
            :param page_url: url地址
            :param soup:
            :return: 返回解析好的数据 url,title,summary
            '''

            res_data = {}

            # url
            res_data['url'] = page_url

            #获取标题内容
            # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1></dd>
            title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")  #获取标题的标签
            res_data['title'] = title_node.get_text()

            #获取简介内容
            # <div class="lemma-summary" label-module="lemmaSummary">  *** </div>
            summary_node = soup.find('div', class_="lemma-summary")
            res_data['summary'] = summary_node.get_text()

            return res_data


        def parse(self, page_url, html_cont):
            '''
            解析器
            :param page_url:   传入一个url
            :param html_cont: 下载好的数据
            :return: 返回解析出新的url列表与数据
            '''


            if page_url is None or html_cont is None:
                return

            soup = BeautifulSoup(html_cont,'html.parser', from_encoding='utf-8')
            new_urls = self._get_new_urls(page_url, soup) #本地方法, 获取url列表
            new_data = self._get_new_data(page_url, soup) #本地方法, 获取数据

            return new_urls,new_data


#
#from html_downloader import HtmlDownloader
#html_download = HtmlDownloader()
#url = 'http://baike.baidu.com/view/21087.htm'
#html_cont = html_download.download(url=url)

#soup = BeautifulSoup(html_cont,'html.parser', from_encoding='utf-8')
#links = soup.find_all('a',href=re.compile(r"/view/\d+\.htm"))  #获取所有的链接
#for link in links:
#    print link['href'],link.get_text()
