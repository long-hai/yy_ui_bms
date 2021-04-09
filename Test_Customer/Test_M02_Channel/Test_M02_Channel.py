# -*- coding:utf-8 -*-
# Author : Longhai
""""
    用例执行
"""
import allure
from business.business_channel import BusinessChannel

# 实例化渠道管理
B_channel = BusinessChannel()


@allure.feature("M02-渠道管理")
class TestChannel(object):

    @allure.story("渠道管理主页")
    def test_channel_home(self, driver):
        B_channel.channel_home(driver)

    @allure.story("新增渠道")
    def test_channel_add(self, driver):
        B_channel.channel_add(driver)

    @allure.story("编辑渠道")
    def test_channel_edit(self, driver):
        B_channel.channel_edit(driver)

    @allure.story("删除渠道")
    def test_channel_delete(self, driver):
        B_channel.channel_delete(driver)
