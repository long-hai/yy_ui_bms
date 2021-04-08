# -*- coding:utf-8 -*-
# Author : Longhai
# 业务封装类
# 客户管理业务模块
import time
import allure
from tools.data import time_tool
from location.base_location import LocationURL, LocationMenu
from location.base_location import LocationCompany, LocationPublic


# 客户管理模块
@allure.feature("客户管理")
class BusinessCompany(object):
    L_menu = LocationMenu
    L_URL = LocationURL
    L_public = LocationPublic
    L_company = LocationCompany

    # 进入客户管理页
    @allure.story("客户管理")
    @allure.title("客户管理首页")
    def company_home(self, driver):
        with allure.step("步骤1：点击客户管理"):
            # 点击客户管理
            driver.click(self.L_menu.menu_company)
            time.sleep(1)
        with allure.step("步骤2：校验是否进入客户管理"):
            title = driver.get_text(self.L_public.public_title)
            # 断言是否进入客户管理页
            assert title == "客户管理" and self.L_URL.URL_company == driver.get_url()
            time_tool.over_time()

    # 添加客户
    @allure.story("客户管理")
    @allure.title("新增客户")
    def company_add(self, driver):
        with allure.step("步骤1：点击新增客户"):
            # 点击新增客户
            driver.click(self.L_company.company_add)
        with allure.step("步骤2：校验是否进入新增客户页面"):
            # 获取页面title
            title = driver.get_text(self.L_public.public_title)
            assert title == "新增客户" and self.L_URL.URL_company_new == driver.get_url()
        with allure.step("步骤3：输入公司信息"):
            # 输入公司信息
            num = "017"
            driver.send_keys(self.L_company.company_name, '自动化测试_{}'.format(num))
            driver.send_keys(self.L_company.company_alias, '自动化测试_{}'.format(num))
            driver.send_keys(self.L_company.company_abbreviation, 'auto_{}'.format(num))
            driver.click(self.L_company.company_type)
            driver.click(self.L_company.company_public)
            driver.send_keys(self.L_company.company_description, 'auto_{}自动化测试，请勿修改操作，谢谢。'.format(num))
        with allure.step("步骤4：点击保存"):
            driver.click(self.L_company.company_save)  # 保存time.sleep(1)
            time.sleep(1)
            error = driver.get_elements(self.L_company.error_class_name)
            success = driver.get_elements(self.L_company.success_class_name)
            # driver.click(L_company.company_cancel)  # 取消
            company_info = driver.get_text(self.L_company.company_first_line)
            company_name = company_info[1]
            assert error == 0 and success == 1 and company_name == "自动化测试_{}".format(num)
