# -*- coding:utf-8 -*-
# Author : Longhai
# 业务封装类
# 订单管理业务模块
import time
import allure
from tools.data import time_tool
from location.base_location import LocationOrder, LocationURL, LocationPublic, LocationMenu


# 订单管理模块
@allure.feature("订单管理")
class BusinessOrder(object):
    L_menu = LocationMenu
    L_URL = LocationURL
    L_oder = LocationOrder
    L_public = LocationPublic

    # 进入订单管理主页
    @allure.story("订单管理")
    @allure.title("订单主页")
    def order_home(self, driver):
        with allure.step("步骤1：点击订单管理"):
            driver.click(self.L_menu.menu_order)  # 点击订单管理
            time.sleep(1)
        with allure.step("步骤2：校验是否进入订单管理"):
            title = driver.get_text(self.L_public.public_title)
            # 断言是否进入订单管理页
            assert self.L_URL.URL_order == driver.get_url() and title == "订单管理"
            time_tool.over_time()

    # 进入新增订单
    @allure.story("订单管理")
    @allure.title("新增订单")
    def order_add(self, driver, channel='Auto_测试渠道', company='AutoT'):
        # 订单信息页
        with allure.step("步骤1：点击新增订单"):
            driver.click(self.L_oder.order_add)
            time.sleep(1)
            elms = driver.get_elements(self.L_oder.order_other)
            # 断言是否进入订单管理页
            assert 2 == elms
        with allure.step("步骤2：填写订单信息"):
            driver.send_keys(self.L_oder.order_channel, '{}'.format(channel))  # 选择渠道
            driver.choose_channel()
            driver.send_keys(self.L_oder.order_company, '{}'.format(company))  # 选择公司
            driver.choose_channel()
            driver.send_keys(self.L_oder.order_description, '{}'.format("自动化测试订单，请勿操作，谢谢。"))  # 填写备注
            driver.choose_channel()
            driver.click(self.L_oder.order_next)  # 点击下一步
            time.sleep(0.5)
        with allure.step("步骤3：校验是否进入订单明细"):  # 订单明细页
            elms = driver.get_elements(self.L_oder.order_other)
            assert 4 == elms  # 断言是否进入订单明细页
        with allure.step("步骤4：填写订单明细"):
            driver.send_keys(self.L_oder.order_search, "A-009S-1-0")
            driver.yy_enter()
            driver.click(self.L_oder.order_courseAdd)
            driver.send_keys(self.L_oder.order_courseNum, "1")
            driver.send_keys(self.L_oder.order_starTime, "2021-04-01")
            driver.send_keys(self.L_oder.order_overTime, "2022-04-01")
            driver.click(self.L_oder.order_next)
            time.sleep(0.5)
        # 提交订单页
        with allure.step("步骤5：校验是否进入提交订单"):
            # 断言是否进入提交订单页
            elms = driver.get_elements(self.L_oder.order_other)
            assert 3 == elms
        # 提交订单
        with allure.step("步骤6：点击提交订单"):
            driver.click(self.L_oder.order_submit)
            driver.click(self.L_oder.order_sure)
            time.sleep(1)
            success = driver.get_text(self.L_oder.order_success)
            assert "新增订单成功！" == success

    # 预览订单
    def order_preview(self, driver):  # self.L_oder
        driver.click(self.L_oder.order_preview)  # 点击预览按钮
        driver.click(self.L_oder.order_detail)

    # 编辑订单
    def order_edit(self, driver):
        driver.click(self.L_oder.order_edit)
        time.sleep(1)
        driver.click(self.L_oder.order_detail)
        driver.send_keys(self.L_oder.order_search, "A-010S-1-0")
        time.sleep(1)
        driver.yy_enter()
        driver.click(self.L_oder.order_courseAdd)
        driver.send_keys(self.L_oder.order_courseNum, "1")
        driver.send_keys(self.L_oder.order_starTime, "2021-04-01")
        driver.send_keys(self.L_oder.order_overTime, "2022-04-01")
        driver.click(self.L_oder.order_save)
        success = driver.get_text(self.L_oder.order_success)
        assert success == "保存成功！"
