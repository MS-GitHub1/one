#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/4 12:30
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm
from selenium.webdriver.common.by import By
class Homepage():
    # 用户名
    name = (By.XPATH, '//input[@name="phone"]')
    # 密码
    password = (By.XPATH,'//input[@name="password"]')
    # 登录按钮
    button = (By.XPATH,'//button[@class="btn btn-special"]')
    # 帮助
    help = (By.XPATH,'//span[@class="no-border"]//a')
    helpop = (By.XPATH,'//div[@class="right fs-12"]//span[@class="no-border"]/a')
    #用户名密码为空
    name_null=(By.XPATH,'//div[@class="form-error-info"]')
    #密码错误
    pws_failed = (By.XPATH,'//div[@class="layui-layer-content"]')
