#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/4 16:08
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm
from Common.basepage import BasePage
from Pagelocators.nmb_index_page import Indexpage as Ba

class IndexPage(BasePage):

    def cl(self):
        self.click_element(Ba.qtb,"点击招投标按钮")

    def jiner(self,money):
        self.send_text(Ba.placeholder,money,"输入对应的金额")
        self.click_element(Ba.button,"点击按钮")

    def tb_successful(self):
       return self.get_element_text(Ba.tbcg,"投标成功")

