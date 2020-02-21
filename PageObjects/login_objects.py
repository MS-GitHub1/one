#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/30 11:04
# @Author  : Lynn
# @Site    :
# @Software: PyCharm

from Common.basepage import BasePage
from Pagelocators.login_page import Homepage as Ba
import time

class LoginPage(BasePage):
    # 元素登陆
    def login(self,username, passwd):
        # 元素等待
        self.click_element(Ba.name,"登陆按钮_登陆按钮")
        self.click_element(Ba.name_login,"登陆界面_点击登陆")
        self.send_text(Ba.userName,username,"")
        self.send_text(Ba.userPassword,passwd,"")
        self.click_element(Ba.Tamgram,"")


    def login_success(self):
        return self.get_element_text(Ba.dl_succesee, "")

    def login_faild(self):
        return self.get_element_text(Ba.pwd_null,"")

    def login_url(self):
        return self.get_current_url(Ba.pwd_null, "")

