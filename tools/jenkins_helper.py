#!/usr/bin/env python
#encoding:utf8
#author: zeping lai

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time

class Jenkins():

    def __init__(self):
        self.driver = webdriver.Firefox()   #使用火狐浏览器

    def __del__(self):
        self.driver.quit()  #退出浏览器

    def login(self,url,username,password):
        '''
        登录jenkins系统平台
        :param url:   登陆地址
        :param username:  登录账号
        :param password:  登录密码
        :return:  登录成功返回True,否则返回False
        '''
        try:
            self.driver.get(url)   #打开浏览器并访问URL地址
            self.driver.find_element_by_id("j_username").clear()
            self.driver.find_element_by_id("j_username").send_keys(username)    #输入帐号
            self.driver.find_element_by_name("j_password").clear()
            self.driver.find_element_by_name("j_password").send_keys(password)  #输入密码
            self.driver.find_element_by_id("yui-gen1-button").click()       #点击登录

            login_info = self.driver.find_element_by_xpath("//div[@class='login']").find_element_by_tag_name("a").get_attribute("href")
            if re.search(r'user',str(login_info)):
                return True
            else:
                return False
        except:
            return False

    def on_aout_refresh_page(self):
        '''
        开启jenkins自动刷新页面
        :return:
        '''
        refresh = self.driver.find_element_by_id("right-top-nav").find_element_by_tag_name("a")
        refresh_status = refresh.get_attribute("href")
        if str(refresh_status).split('=')[1]:
            print "自动刷新页面 - 已开启"
        else:
            print "自动刷新页面 - 正在开启"
            refresh.click()

    def search(self,domain):
        '''
        查询选择job项目，如果有该项目则返回True否则返回False
        :param domain:  网站域名
        :return:  返回网站域名对应的job项目名称，否则返回Flase
        '''

        try:
            # 网站域名
            # domain = 'www.linuxhub.org'

            # job 项目名称
            job = domain + '_online'

            # 查找
            self.driver.find_element_by_id("search-box").clear()
            find = self.driver.find_element_by_id("search-box")
            find.send_keys(domain)
            find.send_keys(Keys.ENTER)
            self.driver.implicitly_wait(30)  # 超时等待

            main_panel = self.driver.find_element_by_xpath("//div[@id='main-panel']")
            # 匹配查找是否包含Nothing，如果有则说明没有这个域名
            if re.search(r'Nothing',main_panel.text):
                return False

            links = main_panel.find_element_by_tag_name("ol").find_elements_by_tag_name("a")
            for link in links:
                link_text = link.get_attribute("text")
                if str(job) == str(link_text):
                        return str(job)
                else:
                        return False
        except:
            return False


    def build(self,job):
        '''
        构建项目，构建成功返回True,否则返回Flase
        :param job: 项目名称
        :return:  构建发布成功则返回True,否则返回Flase
        '''

        try:
            self.driver.find_element_by_link_text(job).click()
            self.driver.implicitly_wait(30)  # 超时等待
            # time.sleep(1)
            self.driver.find_element_by_link_text("立即构建").click()
            # print "正在构建中........"

            # 到控制台详细输出
            self.driver.refresh()  # 刷新页面
            build_history = self.driver.find_element_by_xpath("//table[@class='pane stripped']/tbody/tr[@class='build-row  single-line overflow-checked']").find_element_by_tag_name(
                    "a")
            build_history.click()
            # time.sleep(1)
            self.driver.implicitly_wait(30)  # 超时等待
            self.driver.refresh()
            console_status = ""
            while True:
                console_status = self.driver.find_element_by_xpath("//div[@id='main-panel']/h1").find_element_by_tag_name(
                    'img').get_attribute(
                    "title")
                if console_status:
                    break
                time.sleep(1)
                self.driver.refresh()
                console_status = self.driver.find_element_by_xpath("//div[@id='main-panel']/h1").find_element_by_tag_name(
                    'img').get_attribute(
                    "title")
            # print console_status
            if str(console_status) == "Success":
                return True
            else:
                return False
        except:
            return False



if __name__ == '__main__':

    url = "http://192.168.18.12:8080/login?from=%2F"
    username = "linuxhub"
    password = "123456"
    domain = "www.linuxhub.org"

    jenkins=Jenkins()
    if jenkins.login(url,username,password):
        job = jenkins.search(domain)
        if job:
            if jenkins.build(job):
                print "项目构建成功: " + job
            else:
                print "项目构建失败: " + job
        else:
            print "没有这个项目: " + job
    else:
        print "登录失败"

