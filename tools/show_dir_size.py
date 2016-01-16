#!/usr/bin/env python
#encoding:utf8
#author: zeping lai

import sys
import os
from operator import itemgetter


def hex_conversion(size):
    '''
    Bety 进制转换
    :param size: 输入Bety大小数值
    :return: 返回直观的存储大小
    '''
    if size < 1024 :
        return "%0.2f Bety" %(float(size))

    elif size < 1048576 :
        return "%0.2f KB" %(float(size)/1024)

    elif size < 1073741824 :
        return "%0.2f MB" %(float(size)/1024/1024)

    elif size < 1099511627776:
        return  "%0.2f GB" %(float(size)/1024/1024/1024)
    else:
        return "%0.2f Bety" %(float(size))

def get_dir_size(dir):
    '''
    目录下的文件大小
    :param dir:
    :return: 目录大小,以字节为单位
    '''
    size = 0L
    for root, dirs, files in os.walk(dir,True):
        for name in files:
            size += os.path.getsize(os.path.join(root,name))
    return size

def curr_dir_size(path):
    '''
    当前目录的大小,包含文件
    :param path:
    :return: 目录与文件的大小
    '''

    data_dict = {}
    res_file = {}
    res_dir = {}

    for listdir in os.listdir(path):
        path_listdir = os.path.join(path,listdir)
        if os.path.isfile(path_listdir):
            #print "file:", listdir
            res_file[listdir] = os.path.getsize(path_listdir)
        elif os.path.isdir(path_listdir):
            #print "dir:", listdir
            res_dir[listdir] = get_dir_size(path_listdir)

    data_dict['file'] = res_file
    data_dict['dir'] = res_dir
    return data_dict


def dir_size_sort(path):

    #显示大小排序前几条数据
    head_max = 10

    print "\n您正在查看的目录是: %s" % path
    print "显示大小排行前%s的文件或目录." % head_max

    data = curr_dir_size(path)
    files = data['file']
    if files:
        print "\n文件如下:"
        res_sort = sorted(files.iteritems(), key=itemgetter(1), reverse=True)
        n = 0

        print '',format('','-^60')
        print '| {:<2} | {:<14} | {:<44} |'.format("No", "文件大小", "文件名称")
        print '',format('','-^60')
        for res in res_sort:
            n = n + 1
            print '| {:<2} | {:>10} | {:<40} |'.format(n, hex_conversion(res[1]), res[0])
            if n == head_max:
                break
        print '',format('','-^60')

    dirs = data['dir']
    if dirs:
        print "\n目录如下:"
        res_sort = sorted(dirs.iteritems(), key=itemgetter(1), reverse=True)
        n = 0
        print '',format('','-^60')
        print '| {:<2} | {:<14} | {:<44} |'.format("No", "目录大小", "目录名称")
        print '',format('','-^60')
        for res in res_sort:
            n = n + 1
            print '| {:<2} | {:>10} | {:<40} |'.format(n, hex_conversion(res[1]), res[0])
            if n == head_max:
                break
        print '',format('','-^60')
    print "\n"

if __name__ == "__main__":

    try:
        path = sys.argv[1]
        # path = "/data/down"
        dir_size_sort(path)
    except:
        print "\n请在脚本后面输入目录路径!  "
        print "例: %s /data/down/\n" % sys.argv[0]

