# -*- coding:utf-8 -*-
# Author : Longhai
# 业务封装类
# 报告管理业务模块
import time
import allure
from tools.data import time_tool
from location.base_location import LocationMenu, LocationURL


class BusinessReport(object):
    L_menu = LocationMenu
    L_URL = LocationURL

    def report_home(self, driver):
        with allure.step("步骤1：点击报告管理"):
            driver.click(self.L_menu.menu_report)  # 点击报告管理
            time.sleep(1)
            assert self.L_URL.URL_report == driver.get_url()  # 断言是否进入报告管理页
            time.sleep(1)
            time_tool.over_time()

    def report_team(self, driver):
        with allure.step("步骤1：选择公司"):
            driver.send_keys('//div[@placeholder="所有公司"]', '项目学习')  # 选择公司
            driver.choose_channel()
            driver.send_keys('//input[@placeholder="根据姓名/手机号/账号搜索学员"]', 'XMXXlonghai')  # 搜索学员
            driver.yy_enter()