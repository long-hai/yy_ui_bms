# -*- coding:utf-8 -*-
# Author : Longhai
""""
    用例执行
"""
import allure
from business.business_report import BusinessReport
B_report = BusinessReport()


@allure.feature("M07-学习数据看板")
class TestReport(object):

    @allure.story("学习数据看板主页")
    def test_report_home(self, driver):
        B_report.report_home(driver)
