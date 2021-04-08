# -*- coding:utf-8 -*-
# Author : Longhai
# 业务封装类
# 学员管理业务模块
import time
import allure
import xlrd
from database import db_select
from tools.oss import os_tool
from xlutils3.copy import copy
from tools.data import random_tool, time_tool
from location.base_location import LocationURL, LocationMenu
from location.base_location import LocationStudent


@allure.feature("学员管理")
class BusinessStudent(object):
    L_menu = LocationMenu
    L_URL = LocationURL
    L_stu = LocationStudent

    # 学员管理主页
    @allure.story("学员管理主页")
    @allure.title("学员管理主页")
    @allure.description("登录后运营后台，进入首页，点击学员管理，查看是否正常跳转。")
    def student_home(self, driver):
        with allure.step("步骤1：点击学员管理"):
            driver.click(self.L_menu.menu_student)  # 点击学员管理
            time.sleep(1)
            assert self.L_URL.URL_student == driver.get_url()  # 断言是否进入学员管理页面
            time.sleep(1)

    # 添加学员
    def student_add(self, driver, course=None, channel=None):
        step = 2
        with allure.step("步骤1：点击{}".format(course)):
            driver.click(self.L_stu.stu_choice_course.format(course))  # 点击***课
            time.sleep(1)
        if course == "内训课":
            num = 1
            with allure.step("步骤2：选择公司"):
                driver.send_keys(self.L_stu.stu_choice_company, '{}'.format(channel))  # 选择***
                driver.choose_channel()
            with allure.step("步骤3：点击新增学员"):
                driver.click(self.L_stu.stu_nx_add)  # 点击新增学员
                time.sleep(1)
        elif course == "体验课":
            num = 2
            with allure.step("步骤2：选择渠道"):
                driver.send_keys(self.L_stu.stu_choice_channel, '{}'.format(channel))  # 选择***
                driver.choose_channel()
            with allure.step("步骤3：点击新增学员"):
                driver.click(self.L_stu.stu_other_add)  # 点击新增学员
                time.sleep(0.5)
        else:
            num = 1
            with allure.step("步骤2：点击新增学员"):
                driver.click(self.L_stu.stu_other_add)  # 点击新增学员
                time.sleep(0.5)
        step = step + num
        with allure.step("步骤{}：输入学员信息".format(step)):
            s_company = driver.get_text(self.L_stu.stu_company_name)  # 获取当前公司名称
            company_abbr = driver.get_text(self.L_stu.stu_company_abbr)
            employee_number = int(db_select.get_employe_number(s_company))  # 获取当前渠道学员员工号
            account_number = company_abbr + str(employee_number)  # 获取账号==》断言用
            sex = random_tool.random_sex()
            s_name = "{}_{}".format(company_abbr, employee_number)
            driver.send_keys(self.L_stu.stu_name, "{}".format(s_name))  # 输入学员姓名
            driver.send_keys(self.L_stu.stu_num, "{}".format(employee_number))  # 输入学员员工号
            driver.click(self.L_stu.stu_random_sex.format(sex))  # 选择性别
            driver.send_keys(self.L_stu.stu_phone, '')  # 输入手机号18017694162
            driver.send_keys(self.L_stu.stu_department, '营销部')  # 输入部门
            driver.send_keys(self.L_stu.stu_position, '销售')  # 输入职位
            driver.send_keys(self.L_stu.stu_experience, '2')  # 输入经验年数
            driver.send_keys(self.L_stu.stu_close, '2025-01-01 00:00:00')  # 输入关闭日期
            driver.send_keys(self.L_stu.stu_description, '自动化测试添加学员，请勿操作，谢谢。')  # 输入备注
            driver.click(self.L_stu.stu_choice_tag)  # 选择标签
            driver.click(self.L_stu.stu_choice_all)  # 选择课程
        step = step + 1
        with allure.step("步骤{}：点击保存学员".format(step)):
            driver.click(self.L_stu.stu_save)  # 点击保存学员
            time.sleep(1)

            first_line = self.L_stu.stu_first_line
            if course == "内训课":
                s_course = self.L_stu.stu_nx_course
            elif course == "公开课":
                s_course = self.L_stu.stu_gk_course
            else:
                s_course = self.L_stu.stu_ty_course
                first_line = self.L_stu.stu_ty_first_line
            stu_info = driver.get_text(first_line)
            account_number_now = stu_info[1]
            stu_name = stu_info[0]
            stu_company = stu_info[2]
            stu_course = stu_info[5]
            assert account_number_now == account_number and stu_name == s_name
            assert stu_company == s_company and stu_course == s_course

    @allure.story("学员管理")
    @allure.title("2-搜索学员")
    def student_search(self, driver):
        with allure.step("步骤1：搜索学员"):
            account_after = driver.get_text(self.L_stu.stu_first_account)  # 获取第一个学员账号
            driver.send_keys(self.L_stu.stu_search, account_after)  # 输入一个学员账号
            driver.yy_enter()  # 回车搜索
            time.sleep(1)
            flag = driver.is_ElementExist(self.L_stu.stu_page_num)  # 断言是否搜索到
            assert flag is True
            time.sleep(0.5)

    # 批量激活
    @allure.story("学员管理")
    @allure.title("3-激活学员")
    def student_open(self, driver):
        with allure.step("步骤1：选择激活的学员"):
            driver.click(self.L_stu.stu_check_box)  # 选择激活学员
        with allure.step("步骤2：点击学员菜单"):
            driver.click(self.L_stu.stu_menu)  # 点击学员菜单
        with allure.step("步骤3：点击批量激活"):
            driver.click(self.L_stu.stu_activate)  # 点击批量激活
            time.sleep(1)
            open_stu = driver.get_text(self.L_stu.stu_status)  # 断言激活成功
            assert "有效" == open_stu

    # 批量关闭
    @allure.story("学员管理")
    @allure.title("4-关闭学员")
    def student_close(self, driver):
        with allure.step("步骤1：选择关闭的学员"):
            driver.click(self.L_stu.stu_check_box)  # 选择要关闭的学员
        with allure.step("步骤2：点击学员菜单"):
            driver.click(self.L_stu.stu_menu)  # 点击学员菜单
        with allure.step("步骤3：点击批量关闭"):
            driver.click(self.L_stu.stu_disable)  # 点击批量关闭
            time.sleep(1)
            driver.click(self.L_stu.stu_disable_ok)  # 确定关闭
            time.sleep(0.5)
            close_stu = driver.get_text(self.L_stu.stu_status)  # 断言关闭成功
            assert "无效" == close_stu
            time.sleep(0.5)

    # 编辑学员
    @allure.story("学员管理")
    @allure.title("5-编辑学员")
    def student_edit(self, driver):
        with allure.step("步骤2：点击编辑学员"):
            driver.click(self.L_stu.stu_edit)  # 点击编辑学员
        with allure.step("步骤3：修改学员关闭时间"):
            sex = random_tool.random_sex()
            driver.click(self.L_stu.stu_choice_sex)
            driver.click(self.L_stu.stu_random_sex.format(sex))  # 选择性别
            driver.send_keys(self.L_stu.stu_phone, '')  # 输入手机号18017694162
            driver.send_keys(self.L_stu.stu_department, '技术部')  # 输入部门
            driver.send_keys(self.L_stu.stu_position, '测试')  # 输入职位
            driver.send_keys(self.L_stu.stu_experience, '3')  # 输入经验年数
            driver.send_keys(self.L_stu.stu_close, '2030-01-01 00:00:00')  # 输入关闭日期
            driver.send_keys(self.L_stu.stu_description, '自动化测试编辑学员，请勿操作，谢谢。')  # 输入备注
            elms = driver.get_elements(self.L_stu.stu_course_all) - driver.get_elements(self.L_stu.stu_course_able)
            for index in range(1, elms + 1):
                driver.click(self.L_stu.stu_course_box)
        with allure.step("步骤4：点击保存"):
            driver.click(self.L_stu.stu_save)  # 点击保存
            time.sleep(1)
        with allure.step("步骤5：选择激活的学员"):
            driver.click(self.L_stu.stu_check_box)  # 选择要激活的学员
        with allure.step("步骤6：点击学员菜单"):
            driver.click(self.L_stu.stu_menu)  # 点击学员菜单
        with allure.step("步骤7：点击批量激活"):
            driver.click(self.L_stu.stu_activate)  # 点击批量激活
            time.sleep(1)
            open_stu = driver.get_text(self.L_stu.stu_status)  # 断言激活成功
            assert "有效" == open_stu

    # 预览学员
    @allure.story("学员管理")
    @allure.title("6-预览学员")
    def student_preview(self, driver):
        with allure.step("步骤2：点击预览"):
            driver.click(self.L_stu.stu_preview)  # 点击预览
            time.sleep(0.5)
            flag = driver.is_ElementExist(self.L_stu.stu_preview_title)  # 断言是否进入预览页
            assert flag is True
        with allure.step("步骤3：点击预览"):
            driver.click(self.L_stu.stu_shut)  # 关闭
            driver.get_url()
            assert "studentListNew" in str(driver.get_url())  # 断言是否回到学员管理页面
            time.sleep(1)
            time_tool.over_time()

    # 导出学员
    @allure.story("学员管理")
    @allure.title("7-导出学员")
    def student_export(self, driver):
        self.student_search(driver)
        with allure.step("步骤2：导出学员"):
            driver.click(self.L_stu.stu_check_box)
            driver.click(self.L_stu.stu_menu)
            driver.click(self.L_stu.stu_export)

    # 修改excel数据
    def student_ready(self, driver):
        self.student_search(driver)  # 查找学员
        company = driver.get_text(self.L_stu.stu_home_company_name)  # 获取学员公司
        company_abb = db_select.select_company_abb(company)  # 获取公司缩写
        employee_number = db_select.get_employe_number(company)  # 创建员工号
        name = str(company_abb) + "_" + str(employee_number)  # 创建学员名字
        time.sleep(1)
        rd = xlrd.open_workbook(os_tool.abs_path("./data/data_stu_template/学员导出模板.xlsx"))
        wb = copy(rd)
        # 通过get_sheet()获取有写入的write()方法
        ws = wb.get_sheet(1)
        ws.write(1, 0, name)  # 向名字列写入名字
        ws.write(1, 3, company)  # 写入公司名
        ws.write(1, 7, company_abb)  # 写入公司缩写
        ws.write(1, 8, employee_number)  # 写入员工号
        ws.write(1, 12, "2021-12-31")  # 写入关闭时间
        wb.save(os_tool.abs_path("./data/data_stu_template/学员导出模板.xls"))

    # 导入学员
    @allure.story("学员管理")
    @allure.title("8-导入学员")
    def student_import(self, driver):
        self.student_ready(driver)  # 调用方法
        with allure.step("步骤2：导入学员"):
            driver.click(self.L_stu.stu_menu)
            driver.click(self.L_stu.stu_import)
            driver.file_upload(self.L_stu.stu_upload, os_tool.abs_path("./data/data_stu_template/学员导出模板.xls"))  # 上传文件
            driver.click(self.L_stu.stu_import_ok)
