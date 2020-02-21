#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/4 12:34
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm
from Common.basepage import BasePage
from Pagelocators.nmb_login import Homepage as Ba

class LoginPage(BasePage):
    #正确登录
    def login(self,name,pws):
        self.send_text(Ba.name,name,"输入用户名")
        self.send_text(Ba.password,pws,"输入密码")
        self.click_element(Ba.button,"登录")
    #获取url与相对应的值
    def login_succ(self):
        return self.get_current_url(Ba.help, "url值")
    def login_sussl(self):
        return self.get_element_text(Ba.helpop,"对应的元素值")
    #用户名密码为空
    def name_null(self):
        return self.get_element_text(Ba.name_null,"用户名密码为空")
    #密码错误
    def pws_failed(self):
        return self.get_element_text(Ba.pws_failed,"密码错误")