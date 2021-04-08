# -*- coding:utf-8 -*-
# Author : Longhai
# 业务封装类
# 渠道管理业务模块
import time
import allure
from database import db_select
from tools.data.time_tool import over_time
from location.base_location import LocationURL
from location.base_location import LocationChannel, LocationMenu


# 渠道管理
@allure.feature("渠道管理")
class BusinessChannel(object):
    L_menu = LocationMenu
    L_URL = LocationURL
    L_channel = LocationChannel

    # 进入渠道管理页
    @allure.story("渠道管理")
    @allure.title("渠道管理首页")
    def channel_home(self, driver):
        with allure.step("步骤1：点击渠道管理"):
            driver.click(self.L_menu.menu_channel)  # 点击渠道管理
            time.sleep(1)
            # 断言地址
            assert self.L_URL.URL_channel == driver.get_url()
            time.sleep(1)

    # 新增渠道
    @allure.story("渠道管理")
    @allure.title("新增渠道")
    def channel_add(self, driver):
        with allure.step("步骤1：点击新增渠道"):
            # 点击新增渠道
            driver.click(self.L_channel.channel_add)
        with allure.step("步骤2：输入渠道信息"):
            # 输入渠道名称
            driver.send_keys(self.L_channel.channel_name, "{}".format("自动化测试渠道"))
            driver.click(self.L_channel.channel_tag)
        with allure.step("步骤3：点击保存"):
            driver.click(self.L_channel.channel_save)
            text = driver.get_text(self.L_channel.channel_first_line)
            channel_name = text[1]
            channel_tag = text[2]
            assert channel_name == "自动化测试渠道" and channel_tag == "自动化"

    # 编辑渠道
    @allure.story("渠道管理")
    @allure.title("编辑渠道")
    def channel_edit(self, driver):
        with allure.step("步骤1：点击编辑渠道"):
            # 点击编辑渠道
            driver.click(self.L_channel.channel_edit)
        with allure.step("步骤2：修改渠道名称"):
            # 输入渠道名称
            driver.send_keys(self.L_channel.channel_name, "AUTO自动化测试渠道_UPDATE")
            driver.click(self.L_channel.delete_first_tag)
        with allure.step("步骤3：点击保存"):
            driver.click(self.L_channel.channel_save)
            text = driver.get_text(self.L_channel.channel_first_line)
            channel_name = text[1]
            assert channel_name == "AUTO自动化测试渠道_UPDATE"

    # 删除渠道
    @allure.story("渠道管理")
    @allure.title("删除渠道")
    def channel_delete(self, driver):
        with allure.step("步骤1：点击删除渠道"):
            # 点击删除渠道
            driver.click(self.L_channel.channel_delete)
        with allure.step("步骤2：点击确定"):
            driver.click(self.L_channel.delete_ok)
            time.sleep(1)
            # with allure.step("步骤2：点击取消"):
            #     # 点击取消
            #     driver.click(self.lc.delete_cancel)
            # 断言是否删除渠道
        with allure.step("步骤3：断言是否删除成功"):
            is_channel = db_select.select_channel("AUTO自动化测试渠道_UPDATE")
            assert is_channel == 0
            # 断言是否回到渠道管理页
            assert self.L_URL.URL_channel == driver.get_url()
            time.sleep(1)
            over_time()
