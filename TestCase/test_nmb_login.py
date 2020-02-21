#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/30 10:34
# @Author  : Lynn
# @Site    :
# @Software: PyCharm
from PageObjects.nmb_login import LoginPage
from TestDatas import login_nmb as lo
import pytest
import time
# 默认是用例级别可以不传，如果不是需要传 @pytest.fixture(scope="function")
# 前置条件 使用yield 在yield返回值
@pytest.fixture
def init_driver(init_dr):
    lp = LoginPage(init_dr)
    yield {"driver":init_dr,"lp":lp}

class Test_Nmb_login():
    @pytest.mark.usefixtures('demo')
    @pytest.mark.usefixtures('init_driver')
    # 正确的用户名和密码
    def test_login_1(self,init_driver):
        init_driver["lp"].login(lo.success_data["user"],lo.success_data["passwd"])
        time.sleep(0.5)
        assert (lo.success_data["check"] == init_driver["lp"].login_succ())
        assert ("帮助中心"==init_driver["lp"].login_sussl())
    # 错误用例
    @pytest.mark.parametrize("test_info",lo.wrong_da)
    def test_yh_null_2(self,init_driver,test_info):
        init_driver["lp"].login(test_info["user"],test_info["passwd"])
        time.sleep(0.5)
        assert (test_info["check"]==init_driver["lp"].name_null())
        #密码错误
    @pytest.mark.smoke
    def test_psw_failed(self,init_driver):
        init_driver["lp"].login(lo.pws_failed["user"],lo.pws_failed["passwd"])
        time.sleep(0.5)
        assert (lo.pws_failed["check"]==init_driver["lp"].pws_failed())









