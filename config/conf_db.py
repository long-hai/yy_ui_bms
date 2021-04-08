# -*- coding:utf-8 -*-
# Author : Longhai
import pymysql


def db_test_TH():
    conn = pymysql.connect('47.241.2.253',user = "root",passwd = "123456",db = "dditestinter-new")
    cursor = conn.cursor()
    return cursor,conn

def db_uat_TH():
    conn = pymysql.connect('47.241.2.253',user = "root",passwd = "123456",db = "dditestinter")
    cursor = conn.cursor()
    return cursor,conn


# 中文UAT数据库陪连接配置
def db_uat_ZH():
    conn = pymysql.connect('rm-uf6date0p08219sq43o.mysql.rds.aliyuncs.com',user = "dditest",passwd = "dditest2020",db = "dditest_v5_uat")
    cursor = conn.cursor()
    return cursor,conn


def db_thproddev():
    conn = pymysql.connect('rm-t4njj0sl0p9cee69rio.mysql.singapore.rds.aliyuncs.com',user = "thproddev",passwd = "thproddev2020",db = "thprod")
    cursor = conn.cursor()
    return cursor,conn

def db_trail():
    conn = pymysql.connect('rm-t4njj0sl0p9cee69rio.mysql.singapore.rds.aliyuncs.com',user = "trail",passwd = "trail2020",db = "thtrail")
    cursor = conn.cursor()
    return cursor,conn



