#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/30 09:59
# @Author  : Lynn
# @Site    : 
# @File    : login_page.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

class Homepage:
    # 百度首页登陆按钮
    name = (By.XPATH, '//div[@id="u1"]//a[@name="tj_login"]')
    # 用户登陆按钮
    name_login = (By.XPATH, '//div[@class="tang-pass-footerBar"]//p[@title="用户名登录"]')
    # 用户名
    userName = (By.XPATH, '//input[@name="userName"]')
    #密码
    userPassword = (By.XPATH, '//input[@name="password"]')
    #登陆按钮
    Tamgram = (By.XPATH, '//input[@value="登录"]')
    # 登陆成功
    dl_succesee = (By.XPATH, '//a[@id="s_username_top"]//span')

    pwd_null = (By.ID, 'TANGRAM__PSP_10__errorWrapper')





