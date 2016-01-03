#!/usr/bin/env python
#encoding:utf8
#author: zeping lai
# proc_acti_info.py

import sys,psutil,datetime

def GetPid(pname):
    '''
    根据进程名称获取进程id
    :param pname: 进程名称
    :return: 进程id,或者空列表
    '''
    res = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name'])
        except psutil.NoSuchProcess:
            pass
        else:
            #print(pinfo)
            if pinfo['name'] == pname:
                res.append(pinfo['pid'])
    return res

#print GetPid('php-fpm')


def Date(pname):

    res = {}
    p_time = []
    p_mem = []
    p_pio = []
    p_conn = []
    p_open_file = []
    num = 0
    for pid in GetPid(pname):
        num = num + 1
        p = psutil.Process(pid)

        #内存
        #pextmem(rss=10280960, vms=214900736, shared=3534848, text=9728000, lib=0, data=7585792, dirty=0)
        m = p.memory_info_ex()
        mem = []
        mem.append(num)
        mem.append(pid)
        mem.append(m.rss)
        mem.append(m.vms)
        mem.append(m.shared)
        mem.append(m.text)
        mem.append(m.data)
        p_mem.append(mem)

        #进程IO
        #pio(read_count=196, write_count=15, read_bytes=0, write_bytes=0)
        io = p.io_counters()
        pio = []
        pio.append(num)
        pio.append(pid)
        pio.append(io.read_count)
        pio.append(io.write_count)
        pio.append(io.read_bytes)
        pio.append(io.write_bytes)
        p_pio.append(pio)

        #网络连接

        for n in p.connections():
            conn = []
            conn.append(num)
            conn.append(pid)

            conn.append(n.laddr[0])
            conn.append(n.laddr[1])

            if n.raddr:
                conn.append(n.raddr[0])
                conn.append(n.raddr[1])
            else:
                conn.append('0.0.0.0')
                conn.append('*')
            conn.append(n.status)
            p_conn.append(conn)


        #打开的文件

        for f in p.open_files():
            of = []
            of.append(num)
            of.append(pid)
            of.append(f.path)
            of.append(f.fd)
            p_open_file.append(of)


        #进程时间
        create_time = p.create_time()
        p = []
        p.append(num)
        p.append(pid)
        p.append(create_time)
        p_time.append(p)


    res['t_time'] = p_time
    res['mem'] = p_mem
    res['pio'] = p_pio
    res['conn'] = p_conn
    res['open_file'] = p_open_file
    return res


def main(pname):

    #pname='php-fpm'
    data = Date(pname)

    current_time_list = data['t_time']
    if current_time_list:

        print "\n进程名称: %s" % pname
        current_time = datetime.datetime.now()
        print "当前时间: %s " % current_time.strftime("%Y-%m-%d %H:%M:%S")

        print "\n1.进程创建时间与已运行时间"
        print '',format('','-^56')
        print '| {:<2s} | {:<5} | {:<25} | {:<23} |'.format('No','pid','进程创建时间','运行时间(H:M:S:MS)')
        print '',format('','-^56')
        for t in current_time_list:
            p_create_time = datetime.datetime.fromtimestamp(t[2])
            time_diff = current_time - p_create_time
            c_time = p_create_time.strftime("%Y-%m-%d %H:%M:%S")
            print '| {:<2} | {:<5} | {:<19} | {:<19} |'.format(t[0],t[1],c_time,time_diff)
        print '',format('','-^56')


        print "\n2.进程使用内存信息"
        mem_list = data['mem']
        if mem_list:
            print '',format('','-^71')
            print '| {:<2} | {:<5} | {:<9} | {:<10} | {:<9} | {:<8} | {:<8} |'.format("No","pid","rss","vms","shared","text","data")
            print '',format('','-^71')
            for m in mem_list:
                print '| {:<2} | {:<5} | {:<9} | {:<10} | {:<9} | {:<8} | {:<8} |'.format(m[0],m[1],m[2],m[3],m[4],m[5],m[6])
            print '',format('','-^71')
        else:
             print "没有获取到相关信息."


        print "\n3.进程使用IO信息"
        io_counters_lsit = data['pio']
        if io_counters_lsit:
            print '',format('','-^67')
            print '| {:<2} | {:<5} | {:<10} | {:<11} | {:<11} | {:<11} |'.format("No","pid","read_count","write_count","read_bytes","write_bytes")
            print '',format('','-^67')
            for m in io_counters_lsit:
                print '| {:<2} | {:<5} | {:<10} | {:<11} | {:<11} | {:<11} |'.format(m[0],m[1],m[2],m[3],m[4],m[5])
            print '',format('','-^67')
        else:
             print "没有获取到相关信息."


        print "\n4.进程连接网络信息"
        net_conn_list = data['conn']
        if net_conn_list:
            print '',format('','-^78')
            print '| {:<2} | {:<5} | {:<15} | {:<5} | {:<15} | {:<5} | {:<11} |'.format("No","pid","laddr","lport","raddr","rport","status")
            print '',format('','-^78')
            num = 0
            for n in net_conn_list:
                if len(n):

                    #用于多个进程之间进行换行加上线条
                    num = num + 1
                    if num == 1:
                        init_val = n[0]
                    page_val = n[0]

                    if init_val != page_val:
                        init_val = page_val
                        print '|',format('','-^76'),"|"
                    print '| {:<2} | {:<5} | {:<15} | {:<5} | {:<15} | {:<5} | {:<11} |'.format(n[0],n[1],n[2],n[3],n[4],n[5],n[6])
            print '',format('','-^78')
        else:
            print "没有获取到相关信息."


        print "\n5.进程打开的文件 ( fd #文件描述符)"
        open_file_list = data['open_file']
        if open_file_list:
            print '',format('','-^78')
            print '| {:<2} | {:<5} | {:<2} | {:<58} |'.format("No","pid","fd","path")
            print '',format('','-^78')
            num = 0
            for f in open_file_list:
                if len(f):
                    #用于多个进程之间进行换行加上线条
                    num = num + 1
                    if num == 1:
                        init_val = f[0]
                    page_val = f[0]
                    if init_val != page_val:
                        init_val = page_val
                        print '|',format('','-^76'),"|"
                    print "| %s | %s | %s | %s |" %(
                         "{:<2}".format(f[0]),
                         "{:<5}".format(f[1]),
                         "{:<2}".format(f[3]),
                         "{:<58}".format(f[2])
                    )
            print '',format('','-^78')
        else:
            print "没有获取到相关信息."


    else:
        print "\n您输入的 %s 进程名称不存在! " % pname
    print ""

if __name__ == "__main__":

    try:
        val = sys.argv[1]
        pname = str(val)
        main(pname)
    except:
        print "\n请在脚本后面输入进程名称!  "
        print "例: %s nginx\n" % sys.argv[0]
