# -*- coding:utf-8 -*-
# Author : Longhai
""""
    用例执行
"""
import allure
from business.business_order import BusinessOrder

# 实例化订单管理
B_order = BusinessOrder()


@allure.feature("M04-订单管理")
class TestCompany(object):

    @allure.story("订单管理主页")
    def test_order_home(self, driver):
        B_order.order_home(driver)

    @allure.story("新增订单")
    def test_order_add(self, driver):
        B_order.order_add(driver)

    @allure.story("预览订单")
    def test_order_preview(self, driver):
        B_order.order_preview(driver)

    @allure.story("编辑订单")
    def test_order_edit(self, driver):
        B_order.order_edit(driver)
