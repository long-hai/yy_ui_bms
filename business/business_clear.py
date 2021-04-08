# -*- coding:utf-8 -*-
# Author : Longhai
# 业务封装类
# 清除学员数据业务模块
import time
import allure
from tools.data import time_tool
from location.base_location import LocationMenu, LocationURL


class BusinessClear(object):
    L_menu = LocationMenu
    L_URL = LocationURL

    def clear_home(self, driver):
        with allure.step("步骤1：点击学习数据管理"):
            driver.click(self.L_menu.menu_clear)  # 点击学习数据管理
            time.sleep(1)
            # 断言是否进入学习数据管理页
            assert self.L_URL.URL_clear == driver.get_url()
            time.sleep(1)
            time_tool.over_time()
