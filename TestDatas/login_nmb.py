#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/4 14:02
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm
success_data = {"user": "18684720553", "passwd": "python","check": "http://120.78.128.25:8765/Index/index"}


# 用户名为空/密码为空/用户名格式不正确
wrong_da = [
    #密码为空
    {"user": "18684720553", "passwd": "", "check": "请输入密码"},
    # 用户名密码为空
    {"user": "", "passwd": "", "check": "请输入手机号"},
    #用户名不正确
    {"user": "1583136830", "passwd": "121212", "check": "请输入正确的手机号"}]
    #密码错误
pws_failed = {"user": "18684720553", "passwd": "121212","check":"帐号或密码错误!"}

