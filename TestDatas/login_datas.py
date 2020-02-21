#!/usr/bin/python3
"""
@File    : login_datas.py
@Time    : 2019/12/2 21:41
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""
# 成功用例 - 数据
success_data = {"user": "15732805268", "passwd": "chao1116"}
wrong_datas = {"user": "1583136830", "passwd": "", "check": "请您输入密码"}

# 用户名为空/密码为空/用户名格式不正确
wrong_da = [
    {"user": "1583136830", "passwd": "", "check": "请您输入密码"},
    {"user": "", "passwd": "", "check": "请您输入手机/邮箱/用户名"},
    {"user": "", "passwd": "python", "check": "请您输入手机/邮箱/用户名"}
]
