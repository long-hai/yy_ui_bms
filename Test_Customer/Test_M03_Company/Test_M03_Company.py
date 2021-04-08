# -*- coding:utf-8 -*-
# Author : Longhai
""""
    用例执行
"""
import allure
from business.business_company import BusinessCompany

# 实例化客户管理
B_company = BusinessCompany()


@allure.feature("M3-客户管理")
class TestCompany(object):

    @allure.story("客户管理主页")
    def test_company_home(self, driver):
        B_company.company_home(driver)

    @allure.story("新增客户")
    def test_company_add(self, driver):
        B_company.company_add(driver)
