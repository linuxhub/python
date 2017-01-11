#!/usr/bin/env python
#encoding:utf8
#author: zeping lai

class Process(object):

    def parser(self,res=""):

        if res is None:
            return None

        data_list = []
        matches = res["matches"]
        for matche in matches:
            data = {
                "country_cn": "",
                "country_en": "",
                "city_cn": "",
                "city_en": "",
                "ip": "",
                "service": "",
                "port": "",
                "app": "",
                "hostname": "",
                "os": "",
                "device": ""
            }

            # 国家
            data["country_cn"] = matche["geoinfo"]["country"]["names"]['zh-CN']
            data["country_en"] = matche["geoinfo"]["country"]["names"]['en']

            # 城市
            data["city_cn"] = matche["geoinfo"]["city"]["names"]["zh-CN"]
            data["city_en"] = matche["geoinfo"]["city"]["names"]["en"]

            # IP 地址
            data["ip"] = matche["ip"]

            # 服务
            data["service"] = matche["portinfo"]["service"]

            # 端口
            data["port"] = matche["portinfo"]["port"]

            # 产品名称
            data["app"] = matche["portinfo"]['app']

            # 主机名
            data["hostname"] = matche["portinfo"]['hostname']

            # 操作系统
            data["os"] = matche["portinfo"]['os']

            # 设备类型
            data["device"] = matche["portinfo"]['device']

            #print data
            data_list.append(data)
        return data_list

