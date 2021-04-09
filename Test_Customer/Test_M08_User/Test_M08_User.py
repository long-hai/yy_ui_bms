# -*- coding:utf-8 -*-
# Author : Longhai
""""
    用例执行
"""
import allure
from business.business_user import BusinessUser
B_user = BusinessUser()


@allure.feature("M08-用户管理")
class TestUser(object):

    @allure.story("用户管理主页")
    def test_user_home(self, driver):
        driver.refresh()
        B_user.user_home(driver)
