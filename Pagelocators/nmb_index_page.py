#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/4 16:19
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm
from selenium.webdriver.common.by import By

class Indexpage:
    #招投标按钮
    qtb = (By.XPATH, '//a[@href="/loan/loan_detail/Id/19431.html"and@class="btn btn-special"]')
    #输入金额
    placeholder = (By.XPATH,"//input[contains(@class,'invest-unit-investinput')]")
    #投标按钮
    button = (By.XPATH,'//button[@class="btn btn-special height_style"]')
    # 投标成功
    tbcg = (By.XPATH,'//div[@class="layui-layer-content"]//button[text()="查看并激活"]')

