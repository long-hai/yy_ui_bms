# -*- coding:utf-8 -*-
# Author : Longhai
""""
    用例执行
"""
import allure
from business.business_student import BusinessStudent

# 实例化学员管理
B_stu = BusinessStudent()


@allure.feature("M05学员管理")
class TestStudent(object):

    @allure.story("学员管理主页")
    @allure.title("学员管理主页")
    @allure.description("登录后运营后台，进入首页，点击学员管理，查看是否正常跳转。")
    def test_stu_home(self, driver):
        B_stu.student_home(driver)

    # 内训课测试用例
    # --------------------------------------------------------------------------------------
    @allure.story("学员管理-内训课")
    @allure.title("1-新增学员")
    def test_nx_add(self, driver):
        B_stu.student_add(driver, "内训课", "AutoN")

    @allure.story("学员管理-内训课")
    @allure.title("2-搜索学员")
    def test_nx_search(self, driver):
        B_stu.student_search(driver)

    @allure.story("学员管理-内训课")
    @allure.title("3-激活学员")
    def test_nx_open(self, driver):
        B_stu.student_open(driver)

    @allure.story("学员管理-内训课")
    @allure.title("4-关闭学员")
    def test_nx_close(self, driver):
        B_stu.student_close(driver)

    @allure.story("学员管理-内训课")
    @allure.title("5-编辑学员")
    def test_nx_edit(self, driver):
        B_stu.student_search(driver)
        B_stu.student_edit(driver)

    @allure.story("学员管理-内训课")
    @allure.title("6-预览学员")
    def test_nx_preview(self, driver):
        B_stu.student_search(driver)
        B_stu.student_preview(driver)

    @allure.story("学员管理-内训课")
    @allure.title("7-导出学员")
    def test_nx_export(self, driver):
        B_stu.student_export(driver)

    # @allure.story("学员管理-内训课")
    # @allure.title("8-导入学员")
    # def test_nx_import(self, driver):
    #     B_stu.student_import(driver)

    # 公开课测试用例
    # --------------------------------------------------------------------------------------
    @allure.story("学员管理-公开课")
    @allure.title("1-新增学员")
    def test_gk_add(self, driver):
        driver.refresh()
        B_stu.student_add(driver, "公开课")

    @allure.story("学员管理-公开课")
    @allure.title("2-搜索学员")
    def test_gk_search(self, driver):
        B_stu.student_search(driver)

    @allure.story("学员管理-公开课")
    @allure.title("3-激活学员")
    def test_gk_open(self, driver):
        B_stu.student_open(driver)

    @allure.story("学员管理-公开课")
    @allure.title("4-关闭学员")
    def test_gk_close(self, driver):
        B_stu.student_close(driver)

    @allure.story("学员管理-公开课")
    @allure.title("5-编辑学员")
    def test_gk_edit(self, driver):
        B_stu.student_search(driver)
        B_stu.student_edit(driver)

    @allure.story("学员管理-公开课")
    @allure.title("6-预览学员")
    def test_gk_preview(self, driver):
        B_stu.student_search(driver)
        B_stu.student_preview(driver)

    @allure.story("学员管理-公开课")
    @allure.title("7-导出学员")
    def test_gk_export(self, driver):
        B_stu.student_export(driver)

    # @allure.story("学员管理-公开课")
    # @allure.title("8-导入学员")
    # def test_gk_import(self, driver):
    #     B_stu.student_import(driver)

    # 体验课测试用例
    # --------------------------------------------------------------------------------------
    @allure.story("学员管理-体验课")
    @allure.title("1-新增学员")
    def test_ty_add(self, driver):
        driver.refresh()
        B_stu.student_add(driver, "体验课", "Auto_测试渠道")

    @allure.story("学员管理-体验课")
    @allure.title("2-搜索学员")
    def test_ty_search(self, driver):
        B_stu.student_search(driver)

    @allure.story("学员管理-体验课")
    @allure.title("3-激活学员")
    def test_ty_open(self, driver):
        B_stu.student_open(driver)

    @allure.story("学员管理-体验课")
    @allure.title("4-关闭学员")
    def test_ty_close(self, driver):
        B_stu.student_close(driver)

    @allure.story("学员管理-体验课")
    @allure.title("5-编辑学员")
    def test_ty_edit(self, driver):
        B_stu.student_search(driver)
        B_stu.student_edit(driver)

    @allure.story("学员管理-体验课")
    @allure.title("6-预览学员")
    def test_ty_preview(self, driver):
        B_stu.student_search(driver)
        B_stu.student_preview(driver)

    @allure.story("学员管理-体验课")
    @allure.title("7-导出学员")
    def test_ty_export(self, driver):
        B_stu.student_export(driver)

    # @allure.story("学员管理-体验课")
    # @allure.title("8-导入学员")
    # def test_ty_import(self, driver):
    #     B_stu.student_import(driver)
