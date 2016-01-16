#!/usr/bin/env python
#encoding:utf8
#author: zeping lai
#script_name: get_ip_info.py

import os,sys
import urllib, json
from urllib import urlencode

out_file = os.getcwd()+"/out_ip.txt"

def get_ip_info(ip):
    url = "http://ip.taobao.com/service/getIpInfo.php"
    params = {}
    params['ip'] = ip
    params = urlencode(params)
    content = urllib.urlopen("%s?%s" % (url, params)).read()
    res = json.loads(content)
    if res:
        if res['code'] == 0:
            return res['data']
        else:
            return False
#print get_ip_addr(ip='183.6.167.82')

def write_file(str, out_file=out_file):
    f = open(out_file,"a")
    f.write(str+"\n")
    f.close()

def input_file(file):
    f = open(file,'r')
    lines = f.readlines()
    for line in lines:
        ip = line.strip('\n')
        if ip:
            res = get_ip_info(ip)
            if res:
                country = res['country']
                area = res['area']
                region= res['region']
                city = res['city']
                isp = res['isp']
                data = "| {:<15} | {:<6} | {:<6} | {:<8} | {:<8} | {:<12} |".format(
                    ip,
                    country.encode('utf-8'),
                    area.encode('utf-8'),
                    region.encode('utf-8'),
                    city.encode('utf-8'),
                    isp.encode('utf-8')
                )
                print data
                write_file(data)

            else:
                data = "| {:<15} | {:<5} |".format(ip,"Fail")
                print data
                write_file(data)

if __name__ == "__main__":

    try:
        ip_file = sys.argv[1]
        #ip_file = '/data/develop/python/get_ip_info/ip.txt'
        if os.path.exists(ip_file):
            input_file(file=ip_file)
            print "输出文件: %s" % out_file
        else:
            print "输入的ip列表文件不存在"

    except:
        print "\n请在脚本后面输入ip列表文件!  "
        print "例: %s ip_list.txt\n" % sys.argv[0]
