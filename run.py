#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/31 17:44
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm

# 打标记需要创建“pytest.ini”
# [pytest]
# markers=
#     标记名称
#标记运行  pytest.main(["-m","标记名称"])
from http import server
#
import pytest
pytest.main(["-s","-v","--reruns","0", "--reruns-delay", "5",
             "--html=D:/Interface/Automation Framework/reportone/pytest_report.html",
             "--alluredir=D:\Interface\Automation Framework/al/all"]
            )

