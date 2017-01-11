#!/usr/bin/env python
#encoding:utf8
#author: zeping lai

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from model import Host
from model import db


class Outputer(object):

    def storage(self,data_list,page):

        if data_list is None:
            return None

        for row in data_list:
            ip = row["ip"]
            host = Host.query.filter_by(ip=ip).first()
            if host is None:
                host = Host()
                host.page = int(page)
                host.ip = ip
                host.app = row["app"]
                host.port = row["port"]
                host.service = row["service"]
                host.device = row["device"]
                host.hostname = row["hostname"]
                host.os = row["os"]
                host.city_cn = row["city_cn"]
                host.city_en = row["city_en"]
                host.country_cn = row["country_cn"]
                host.country_en = row["country_en"]

                db.session.add(host)
                db.session.commit()
                #print host

#outputer = Outputer()
#outputer.storage(data_list)
