# -*- coding:utf-8 -*-
# Author : Longhai
""""
    用例执行
"""
import allure
from business.business_clear import BusinessClear
B_clear = BusinessClear()


@allure.feature("M09-学习数据管理")
class TestClear(object):

    @allure.story("学习数据管理主页")
    def test_clear_home(self, driver):
        B_clear.clear_home(driver)
