#!/usr/bin/env python
#encoding:utf8
#author: zeping lai

import os, sys
import pycurl

def main(url):

    c= pycurl.Curl() #创始一个Curl对象http://ksadmin.youxilaile.com/api/gp/get_ali_notify
    c.setopt(pycurl.URL, url) #定义请求的URL
    c.setopt(pycurl.CONNECTTIMEOUT, 5) #连接等等时间
    c.setopt(pycurl.TIMEOUT, 5)         #请求超时时间
    c.setopt(pycurl.NOPROGRESS, 1)     #屏蔽下载进度条
    c.setopt(pycurl.FORBID_REUSE, 1)   #完成交互后强制断开连接,不重用
    c.setopt(pycurl.MAXREDIRS, 1)      #指定HTTP重定向的最大数
    c.setopt(pycurl.DNS_CACHE_TIMEOUT, 30) #设置保存DNS信息时间,默认为120秒


    #创建一个文件对象
    indexfile = open(os.path.dirname(os.path.realpath(__file__))+"/content.txt","wb")
    c.setopt(pycurl.WRITEHEADER, indexfile) #返回的HTTP HERADER写到文凭
    c.setopt(pycurl.WRITEDATA, indexfile)   #返回的HTML内容写到文件

    try:
        c.perform() #提交
    except Exception,e:
        print "连接出错:"+str(e)
        indexfile.close()
        c.close()
        sys.exit()

    namelookup_time = c.getinfo(c.NAMELOOKUP_TIME) #获取DNS解析时间
    connect_time = c.getinfo(c.CONNECT_TIME)       #获取建立连接时间
    pretransfer_time = c.getinfo(c.PRETRANSFER_TIME)     #获取从建立连接到准备传输所消耗的时间
    starttransfer_time = c.getinfo(c.STARTTRANSFER_TIME) #获取从建立连接到传输开始消耗的时间
    total_time = c.getinfo(c.TOTAL_TIME)         #获取传输总时间

    http_code = c.getinfo(c.HTTP_CODE)           #获取http状态码
    size_download = c.getinfo(c.SIZE_DOWNLOAD)   #获取下载数据包大小
    header_size = c.getinfo(c.HEADER_SIZE)       #获取http头部大小
    speed_download = c.getinfo(c.SPEED_DOWNLOAD) #获取平均下载速度

    #打印相关数据
    print "\nURL地址: %s" %(url)
    print "HTTP状态码: %s" %(http_code)
    print "DNS解析时间: %.2f ms" %(namelookup_time)
    print "建立连接时间: %.2f ms" %(connect_time)
    print "准备传输时间: %.2f ms" %(pretransfer_time)
    print "开始传输时间: %.2f ms" %(starttransfer_time)
    print "传输结束时间: %.2f ms" %(total_time)
    print "下载数据包大小: %d bytes/s" %(size_download)
    print "HTTP头部大小: %d byte" %(header_size)
    print "平均下载速度: %d bytes/s\n" %(speed_download)

    #关闭文件及Curl对象
    indexfile.close()
    c.close()


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        # url = "http://www.linuxhub.org"
        main(url)
    except:
        print "\n请在脚本后面输入url地址!  "
        print "例: %s http://www.linuxhub.org\n" % sys.argv[0]
