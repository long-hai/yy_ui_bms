# -*- coding:utf-8 -*-
# Author : Longhai
import pytest
from config.conf_case import Complete, Login, Channel, Company, Order
from config.conf_case import Student, Study, Report, User, Clean, Password
from tools.oss.os_tool import deldir
from tools.oss import shell_tool, os_tool

if __name__ == '__main__':
    # 清除报告
    deldir(os_tool.abs_path("./reports/xml"))
    deldir(os_tool.abs_path("./reports/html"))

    # 测试用例路径
    test_case = os_tool.abs_path("./test_customer/TEST_01_LOGIN/TEST_01_LOGIN.py")

    # 报告保存路径
    xml_report_path = os_tool.abs_path("./reports/xml")
    html_report_path = os_tool.abs_path("./reports/html")

    # 主方法  Login, Student, Study, Report,User,Clean,Password
    pytest.main(['-s', '-q', '--alluredir', xml_report_path, Complete])
    cmd1 = 'allure generate %s -o %s --clean' % (xml_report_path, html_report_path)
    shell_tool.invoke(cmd1)
