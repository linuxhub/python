#!/usr/bin/env python
#encoding:utf8
#author: zepinglai
#sript name: sftp_update.py

import paramiko
import os

hostname = '192.168.0.202'
username = 'root'
port = 22
key_file = 'key/id_rsa' #私钥文件
key_file_pwd = '123456'  #私钥密码
known_hosts = 'key/known_hosts'
logs_file = 'logs/sftp_up.log' #日志文件


local_path = 'update/test01.txt'  #本地路径（要上传的文件）
remote_path = '/data/tmp/test01.txt' #远程路径


paramiko.util.log_to_file(logs_file)
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

    sftp.put(local_path,remote_path) #上传文件

    t.close()
except Exception,e:
    print str(e)
