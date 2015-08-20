#!/usr/bin/env python
#encoding:utf8
#author: zepinglai
#sript name: key_sftp_down_to_mkdir.py

import paramiko
import os

def key_sftp_down(hostname,username,port,key_file,key_file_pwd,remote_file,down_path):
    '''
    密钥ssh连接方式下载主机文件
    :param hostname:  主机IP地址
    :param username:  用户名
    :param port:      端口
    :param key_file:  私钥文件
    :param key_file_pwd:   私钥密码
    :param remote_file:  远程主机文件(列表类型)
    :param down_path:    本地路径(是目录不是具体的文件)
    :return:   0 表示下载成, 2表示下载出错
    '''

    #判断数据类型是否为list类型
    if isinstance(remote_file,list) == False:
        #print "您输入的数据不对,请输入列表类型!"
        return 2

    privatekey = os.path.expanduser(key_file)
    try:
        key = paramiko.RSAKey.from_private_key_file(privatekey)
    except paramiko.PasswordRequiredException:
        #需要密钥口令
        key = paramiko.RSAKey.from_private_key_file(key_file,key_file_pwd)

    try:
        t = paramiko.Transport((hostname,port))
        t.connect(username=username,pkey=key)
        sftp = paramiko.SFTPClient.from_transport(t)

        for remote_file_path in remote_file:

            #取出目录并判断目录是否存在,不存在则创建
            down_file_path = down_path+remote_file_path
            down_dir = os.path.dirname(down_file_path)
            if not os.path.exists(down_dir):
                os.makedirs(down_dir)

            #下载文件
            if sftp.get(remote_file_path,down_file_path) == None:
                #print "下载成功 %s" %(remote_file_path)
                pass
        t.close()
        return 0

    except Exception,e:
        #print str(e)
        #print "下载出错 %s" %(remote_file_path)
        return 2






#测试该方法
if __name__ == '__main__':

    hostname = '192.168.0.202'
    username = 'root'
    port = 22
    key_file = 'key/id_rsa' #私钥文件
    key_file_pwd = 123456''  #私钥密码
    down_path = 'down'  #本地路径（下载的路径目录）
    remote_file = ['/data/tmp/test01.txt','/data/tmp/test02.txt','/data/tmp/test03.txt'] #远程路径

    code = key_sftp_down(hostname,username,port,key_file,key_file_pwd ,remote_file,down_path)

    if code == 0:
        print "下载成功"
    elif code == 2:
        print "下载出错"







