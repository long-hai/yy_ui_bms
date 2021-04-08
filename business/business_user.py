# -*- coding:utf-8 -*-
# Author : Longhai
# 业务封装类
# 用户管理业务模块
import time
import allure
from tools.data import time_tool
from location.base_location import LocationMenu, LocationURL


class BusinessUser(object):
    L_menu = LocationMenu
    L_URL = LocationURL

    def user_home(self, driver):
        with allure.step("步骤1：点击用户管理"):
            driver.click(self.L_menu.menu_user)  # 点击用户管理
            time.sleep(1)
            assert self.L_URL.URL_user == driver.get_url()  # 断言是否进入用户管理页
            time.sleep(1)
            time_tool.over_time()
