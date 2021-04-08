# -*- coding:utf-8 -*-
# Author : Longhai
# 业务封装类
# 登录业务模块
import time
import allure
from location.base_location import LocationURL
from location.base_location import LocationLogin


# 登录模块
@allure.story("登录模块")
@allure.title("用户登录")
class BusinessLogin(object):
    L_URL = LocationURL
    L_login = LocationLogin

    def login_home(self, driver, user="longhai", password="q123456"):
        with allure.step("步骤1：打开网址"):
            driver.get(self.L_login.login_URL)
        with allure.step("步骤2：输入账号密码"):
            driver.send_keys(self.L_login.login_userName, user)
            driver.send_keys(self.L_login.login_password, password)
        with allure.step("步骤3：点击登录"):
            driver.click(self.L_login.login_button)
            time.sleep(1)
            assert self.L_URL.URL_base in driver.get_url()
