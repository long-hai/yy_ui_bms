# -*- coding:utf-8 -*-
# Author : Longhai
import os
import shutil
from tools.data.time_tool import over_time


# 删除报告文件
def rm_file():
    isHave = os.path.exists("../../reports/xml")
    if isHave:
        # shutil.rmtree("../../reports/xml")
        print("测试")
        over_time()


# 删除文件下所有文件
def yy_rm(excel_path):
    isHave = os.path.exists(excel_path)
    if isHave:
        shutil.rmtree(excel_path)

# 判断文件是否存在
def yy_have(excel_path):
    isHave = os.path.exists(excel_path)
    return isHave

