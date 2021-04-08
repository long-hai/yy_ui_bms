# -*- coding:utf-8 -*-
# Author : Longhai
# 业务封装类
# 权限业务模块
import allure
from business.business_login import BusinessLogin
from config import conf_system
from location.base_location import LocationURL
from location.base_location import LocationPermission as L_permission


# 权限业务模块
from tools.data.yaml_tool import get_yaml
from tools.oss import os_tool


class BusinessPermission(object):
    L_URL = LocationURL
    Login = BusinessLogin()

    # 用户登录（权限校验）
    @allure.story("登录模块")
    @allure.title("用户登录-权限校验")
    def login_permission(self, driver):
        user = get_yaml(os_tool.abs_path("./data/data_login_user/yaml_user.yaml"))
        for i in user:
            username = user[i]["name"]
            password = user[i]["pwd"]
            self.Login.login_home(driver, username, password)
            with allure.step("步骤4：登录校验"):
                elms = driver.get_elements("el-tooltip")  # 获取用户权限icon个数
                menus_class = []
                for i in range(1, int(elms) + 1):
                    s = driver.get_attribute(L_permission.permission_menu.format(i), "class")  # 循环获取权限icon的className
                    menus_class.append(s)
                user_info = driver.get_text(L_permission.permission_user_info)  # 获取用户角色名称
                role_name = str(user_info).split(" ")[0]
                with allure.step("步骤5：角色校验==>当前角色为:[{}]".format(role_name)):
                    if role_name == "管理员":
                        assert conf_system.ADMIN_ROLE == menus_class and driver.get_url() == self.L_URL.URL_channel
                    elif role_name == "LEAF渠道负责人":
                        assert conf_system.LEAF_QD_ROLE == menus_class and driver.get_url() == self.L_URL.URL_channel
                    elif role_name == "渠道负责人":
                        assert conf_system.QUDAO_ROLE == menus_class and driver.get_url() == self.L_URL.URL_channel
                    elif role_name == "项目经理":
                        assert conf_system.XMJL_ROLE == menus_class and driver.get_url() == self.L_URL.URL_company
                    elif role_name == "公开课项目负责人":
                        assert conf_system.GKK_ROLE == menus_class and driver.get_url() == self.L_URL.URL_student
                    elif role_name == "外部渠道运营":
                        assert conf_system.WBQD_ROLE == menus_class and driver.get_url() == self.L_URL.URL_report
                    elif role_name == "HR":
                        assert conf_system.HR_ROLE == menus_class and driver.get_url() == self.L_URL.URL_study
