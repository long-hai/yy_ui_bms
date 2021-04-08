# -*- coding:utf-8 -*-
# Author : Longhai
from time import sleep
from config import conf_system
from test_m_transtalent.test_m_login.test_before import before


def test_m_login(driver):
    # 打开网址
    driver.get("http://m-uat.transtalent.cn/new-login")
    driver.click('//span[text()="使用账号登录 >"]')
    driver.send_keys('//input[@placeholder="请输入账号"]', 'lh20')
    driver.send_keys('//input[@placeholder="请输入密码"]', '20')
    driver.click('//button[@class="submitBtn_3 fontSize16 lineHeight24"]')
    sleep(2)


