# -*- coding:utf-8 -*-
# Author : Longhai
# 业务封装类
# 学习数据看板业务模块
import time
import allure
from tools.data import time_tool
from location.base_location import LocationMenu, LocationURL, LocationStudy


class BusinessStudy(object):
    L_menu = LocationMenu
    L_URL = LocationURL
    L_study = LocationStudy

    def study_home(self, driver):
        with allure.step("步骤1：点击学习数据看板"):
            driver.click(self.L_menu.menu_study)  # 点击学习数据看板
            time.sleep(1)
            assert self.L_URL.URL_study == driver.get_url()  # 断言是否进入学习数据看板页
            time.sleep(1)
            time_tool.over_time()

    def study_team(self, driver):
        with allure.step("步骤1：选择公司"):
            driver.send_keys(self.L_study.study_team_company, '项目学习')  # 选择公司
            driver.choose_channel()
            driver.click(self.L_study.study_team_query)  # 团体查询
            time.sleep(1)
            driver.click(self.L_study.study_time)  # 学习时长
            driver.click(self.L_study.study_team_download)  # 下载团体数据

    def study_single(self, driver):
        driver.refresh()
        with allure.step("步骤1：选择公司"):
            driver.click(self.L_study.study_singles)  # 点击个人数据
            driver.send_keys(self.L_study.study_single_company, '项目学习')  # 选择公司
            driver.choose_channel()
            driver.send_keys(self.L_study.study_single_search, 'XMXXlonghai')  # 搜索学员
            driver.yy_enter()
            driver.click(self.L_study.study_unfold)
            driver.click(self.L_study.study_unfold)
            driver.click(self.L_study.study_single_download)  # 下载个人数据
