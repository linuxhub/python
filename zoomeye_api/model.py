#!/usr/bin/env python
#encoding:utf8
#author: zeping lai

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 数据库配置
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345678@192.168.100.200:3306/zoomeye'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

# 数据表模型
class Host(db.Model):
    __tablename__ = 'host'
    id = db.Column(db.Integer,primary_key=True)       # id 主键自增
    ip = db.Column(db.String(200),index=True)         #IP 地址
    service = db.Column(db.String(200),index=True)    #服务
    port = db.Column(db.Integer)                     #端口
    app = db.Column(db.String(200),index=True)       #产品名称
    hostname = db.Column(db.String(200),index=True)  #主机名称
    device = db.Column(db.String(200),index=True)    #设备类型
    os = db.Column(db.String(200),index=True)        #操作系统

    country_cn = db.Column(db.String(200),index=True)      #国家
    country_en = db.Column(db.String(200),index=True)      #国家
    city_cn = db.Column(db.String(200),index=True)         #城市
    city_en = db.Column(db.String(200),index=True)         #城市

    page = db.Column(db.Integer)  # 采集的页数
    password  = db.Column(db.String(200))         #密码
    is_login = db.Column(db.Boolean, default=False)  # 是否可以登录 (1表示为可以, 0表示不可以)
    remark = db.Column(db.Text)  # 备注

    def __repr__(self):
        return '<Host %r>' % self.ip

# db.drop_all()   #删除所有表
# db.create_all()  #创建所有表




