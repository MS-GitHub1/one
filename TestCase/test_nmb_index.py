#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/4 16:09
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm
import time
import pytest
from PageObjects.nmb_index import IndexPage
# 默认是用例级别可以不传，如果不是需要传 @pytest.fixture(scope="function")
# 前置条件 使用yield 在yield返回值
@pytest.fixture
def init_driver(init_drd):
    lp = IndexPage(init_drd)
    yield {"lp":lp}

class Test_Nmb_index():
    @pytest.mark.usefixtures('demo')
    @pytest.mark.usefixtures('init_driver')
    def test_index(self,init_driver):
        init_driver["lp"].cl()
        init_driver["lp"].jiner(2000)
        time.sleep(2)
        assert ("查看并激活"==init_driver["lp"].tb_successful())














