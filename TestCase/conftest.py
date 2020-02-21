#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/1 14:47
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm
# 共享机制的文件名为conftest.py
import pytest
from selenium import webdriver
from PageObjects.nmb_login import LoginPage
from TestDatas import Common_Datas as AC
@pytest.fixture(scope="class")
def demo():
    print("======================================================================================用例开始=====================================================================================================================")
    yield
    print("======================================================================================用例结束=====================================================================================================================")

@pytest.fixture
def init():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(AC.base_url)
    yield driver
    #后置条件
    driver.quit()

@pytest.fixture
def init_dr():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(AC.login_url)
    yield driver
    #后置条件
    driver.quit()

@pytest.fixture
def init_drd():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(AC.login_url)
    LoginPage(driver).login(AC.user, AC.passwd)
    yield driver
    #后置条件
    driver.quit()

