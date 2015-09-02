#!/usr/bin/env python
#encoding:utf8
#author: zeping lai
#yum install nmap  #系统中安装nmap工具
#pip install python-nmap #python安装nmap模块

import nmap

#扫描在线的主机tcp端口
def ScanHostPort(ip_range,port_range):

    ''' ip_range #IP地址或地址范围 例: 192.168.0.100-200 或 192.168.0.0/24
        poet_range #端口或端口范围, 例: 22,80,443,3306
       返回 :  在线的主机,与开放的端口
    '''

    proto = 'tcp' #当前只能tcp协议
    nm = nmap.PortScanner()
    #调用扫描方法，参数指定扫描主机hosts，nmap扫描命令行参数arguments
    nm.scan(hosts=ip_range, arguments=' -v -sS -p '+port_range)

    if len(nm.all_hosts()):
        for hosts in nm.all_hosts():
            state = nm[hosts].state() #主机机状态
            if state == 'up':
                ip = nm[hosts]['addresses']['ipv4'] #主机IP地址(ipv4)
                try:
                    mac = nm[hosts]['addresses']['mac']  #主机MAC地址
                except:
                    mac = 'None'
                    
                open_port_list = []
                port_list = nm[hosts][proto].keys()  # tcp协议的端口
                port_list.sort()
                for port in  port_list:
                    port_state = nm[hosts][proto][port]['state'] #tcp协议端口状态
                    if port_state == 'open':
                        #print "port: %s" % port
                        open_port_list.append(port)
                
                print "\n"
                print "ip: %s" % ip
                print "mac: %s" % mac
                
                if len(open_port_list):
                    #print open_port_list
                    open_port = str(open_port_list)[1:-1]
                    print "port: %s" % open_port

                else:
                    open_port = 'None'
                    print "port: %s" % open_port
    else:
        print "您输入的IP地址不正确!"



if __name__ == '__main__':
    ip_range = '192.168.0.161-200'
    port_range = '22,80,53,8080,3306'
    ScanHostPort(ip_range,port_range)
