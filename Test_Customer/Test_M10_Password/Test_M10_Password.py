# -*- coding:utf-8 -*-
# Author : Longhai
""""
    用例执行
"""
import allure
from business.business_password import BusinessPassword
B_pwd = BusinessPassword()


@allure.feature("M10-学习数据管理")
class TestPassword(object):

    @allure.story("学习数据管理主页")
    def test_password_home(self, driver):
        B_pwd.password_home(driver)
