# -*- coding:utf-8 -*-
# Author : Longhai
from config import conf_db

cursor, conn = conf_db.db_uat_ZH()
#  获取新增学员的账号
def get_employe_number(company):
    sql = "SELECT (employee_number) FROM company_users WHERE employee_number REGEXP '^[0-9]+$' AND `company_id` = (SELECT `id` FROM `companies` WHERE `name` = '{}');".format(company)
    cursor.execute(sql)
    employee_number = cursor.fetchall()
    data = []
    for i in employee_number:
        data.append(int(i[0]))
    for x in range(10000):
        if x not in data:
            return x


# 获取导入学员的名字和账户
def get_import(company, number):
    sql = "SELECT (employee_number) FROM company_users WHERE employee_number REGEXP '^[0-9]+$' AND `company_id` = (SELECT `id` FROM `companies` WHERE `name` = '{}');".format(company)
    cursor.execute(sql)
    employee_number = cursor.fetchall()
    data = []
    for i in employee_number:
        data.append(i[0])
    while True:
        if str(number) in data:
            number += 1
        else:
            return number



# 查询当前公司的缩写
def select_company_abb(company):
    sql = "SELECT `abbreviation` FROM `companies` WHERE `name` = '{}';".format(company)
    cursor.execute(sql)
    company_abb = cursor.fetchone()
    return company_abb[0]


# 查询渠道是否删除
def select_channel(channel_name):
    sql = "SELECT COUNT(*) FROM `yy_channel_info` WHERE `channel_name` = '{}';".format(channel_name)
    cursor.execute(sql)
    channel_num = cursor.fetchone()
    return int(channel_num[0])

# 查询标签
def select_tag(channel_name):
    sql = "".format(channel_name)
    cursor.execute(sql)
    channel_num = cursor.fetchone()
    return int(channel_num[0])






