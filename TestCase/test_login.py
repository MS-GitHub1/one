#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/30 10:34
# @Author  : Lynn
# @Site    :
# @Software: PyCharm
from PageObjects.login_objects import LoginPage
from TestDatas import login_datas as lo
import pytest
# 默认是用例级别可以不传，如果不是需要传 @pytest.fixture(scope="function")
# 前置条件 使用yield 在yield返回值
@pytest.fixture
def init_driver(init):
    lp = LoginPage(init)
    yield {"driver":init,"lp":lp}


class TestLogin():
    # 传数据为@pytest.mark.usefixtures(),传前置后置条件
    @pytest.mark.usefixtures("demo")
    @pytest.mark.usefixtures("init_driver")
    def test_login_1(self,init_driver):
        init_driver["lp"].login(lo.wrong_datas["user"], lo.wrong_datas["passwd"])
        assert (lo.wrong_datas["check"]==init_driver["lp"].login_faild())

    # 传数据为@pytest.mark.usefixtures(),传前置后置条件
    @pytest.mark.usefixtures("demo")
    @pytest.mark.usefixtures("init_driver")
    @pytest.mark.parametrize("test_info",lo.wrong_da)
    # pytest的数据驱动  @pytest.mark.parametrize("test_info",lo.wrong_da) lo.wrong_da列表数据
    def test_faild_2(self,init_driver,test_info):
        init_driver["lp"].login(test_info["user"],test_info["passwd"])
        assert (test_info["check"]==init_driver["lp"].login_faild())
        assert ("https://www.baidu.com/"==init_driver["lp"].login_url())





