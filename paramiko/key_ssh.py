#!/usr/bin/env python
#encoding:utf8
#author: zepinglai

import paramiko
import os

hostname = '192.168.0.202'
username = 'root'
port = 22
key_file = 'key/id_rsa' #私钥文件
key_file_pwd = '123456'  #私钥密码
known_hosts = 'key/known_hosts'
logs_file = 'logs/ssh_login.log' #日志文件

paramiko.util.log_to_file(logs_file)
privatekey = os.path.expanduser(key_file)
try:
    key = paramiko.RSAKey.from_private_key_file(privatekey)
except paramiko.PasswordRequiredException:
    #需要密钥口令
    key = paramiko.RSAKey.from_private_key_file(key_file,key_file_pwd)

ssh = paramiko.SSHClient()
ssh.load_system_host_keys(filename=known_hosts)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname=hostname,username=username,port=port,pkey=key)
stdin,stdout,stderr = ssh.exec_command("ifconfig")

print stdout.read()

ssh.close()
