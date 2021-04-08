# -*- coding:utf-8 -*-
# Author : Longhai
""""
    用例执行
"""
import allure
from business.business_permission import BusinessPermission

# 实例化登录-权限校验
B_permission = BusinessPermission()


@allure.feature("M1-登录")
class TestPermission(object):

    @allure.story("登录-校验权限")
    def test_permission(self, driver):
        B_permission.login_permission(driver)
