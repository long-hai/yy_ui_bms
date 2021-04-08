# -*- coding:utf-8 -*-
# Author : Longhai
""""
    用例执行
"""
import allure
from business.business_study import BusinessStudy
B_study = BusinessStudy()


@allure.feature("M06-学习数据看板")
class TestStudy(object):

    @allure.story("学习数据看板主页")
    def test_study_home(self, driver):
        B_study.study_home(driver)
