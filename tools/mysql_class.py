#!/usr/bin/env python
#encoding:utf8
#author: zeping lai

import MySQLdb

class Mysql():

    conn = ''
    cursor = ''

    #构造函数
    def __init__(self,conf=''):

        try:
            self.conn = MySQLdb.Connect(
            host = conf['host'],
            port = int(conf['port']),
            user = conf['user'],
            passwd = conf['passwd'],
            db = conf['db'],
            charset = conf['charset']
            )
            if self.conn:
                self.cursor = self.conn.cursor()
        except Exception as e:
            print e

    #查询所有数据
    def fetch_all(self,sql):
        if self.conn:
            try:
                self.cursor.execute(sql)
                return self.cursor.fetchall()
            except Exception as e:
                print e
                return False

    # 返回 SQL语句查询结果中包含的行数
    def count(self,sql):
        if self.conn:
            try:
                self.cursor.execute(sql)
                return self.cursor.rowcount
            except Exception as e:
                print e
                return False

    #增加数据
    def add(self,sql):
        if self.conn:
            try:
                self.cursor.execute(sql)
                self.conn.commit()
                return self.cursor.rowcount
            except Exception as e:
                print e
                return False

    #返回最近插入的自增ID
    def last_insert_id(self):
        if self.conn:
            try:
                return self.cursor.lastrowid
            except Exception as e:
                print e
                return False


    #更新数据
    def update(self,sql):
        return self.add(sql)

    #删除数据
    def delete(self,sql):
        return self.add(sql)

    #析构函数释放连接资源
    def __del__(self):
          if self.cursor:
              self.cursor.close()
          if self.conn:
            self.conn.close()


if __name__ == '__main__':

    conf = {
        'host':'127.0.0.1',
        'port':'3306',
        'user':'root',
        'passwd':'password',
        'db':'linxuhub_db',
        'charset':'utf8'
        }

    mysql = Mysql(conf)

    # 1.查询所有数据
    sql_select = "select * from user"
    res = mysql.fetch_all(sql_select)
    if res:
        for x in res:
            print x[1]
    else:
        print "没有查询出或者查询出错"



    # 统计行数
    '''
    sql_count = "select * from user"
    res = mysql.count(sql_count)
    print "数据行数: %s" % res
    '''

    # 2.增加
    '''
    sql_insrt = "insert into user(userid, username) values(15,'name15')"
    res = mysql.add(sql_insrt)
    if res:
        print "插入数据的行数: %s" % res
        print "返回最近插入的自增ID: %s" % mysql.last_insert_id()
    else:
        print "插入数据失败"
    '''


    # 更新
    '''
    sql_update = "update user set username='name300' where userid=3"
    res = mysql.update(sql_update)
    print res
    if res:
        print "更新数据的行数: %s" % res
    else:
        print "更新数据失败"
    '''

    # 删除
    '''
    sql_delete = "delete from user where userid=3"
    res = mysql.delete(sql_delete)
    print res
    if res:
        print "删除数据的行数: %s" % res
    else:
        print "删除数据失败"
    '''




