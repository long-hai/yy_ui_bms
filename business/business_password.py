# -*- coding:utf-8 -*-
# Author : Longhai
# 业务封装类
# 修改密码业务模块
import time
import allure
from tools.data import time_tool
from location.base_location import LocationMenu, LocationURL


class BusinessPassword(object):
    L_menu = LocationMenu
    L_URL = LocationURL

    def password_home(self, driver):
        with allure.step("步骤1：点击修改密码"):
            driver.click(self.L_menu.menu_password)  # 点击修改密码
            time.sleep(1)
            # 断言是否进入修改密码页
            assert self.L_URL.URL_password == driver.get_url()
            time.sleep(1)
            time_tool.over_time()
