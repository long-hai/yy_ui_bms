# -*- coding:utf-8 -*-
# Author : Longhai

"""
新官网登录页：http://www1.transtalent.cn/index.php/yylogin/，
新官网留资页：http://www1.transtalent.cn/index.php/contacts/，
新官网二维码关注页：http://www1.transtalent.cn/index.php/success/
新官网注销方法：http://www1.transtalent.cn/wp-admin

"""

click_login_event_num = 0

def test_login(driver):
    # 打开网址
    driver.get('https://www1.transtalent.cn/')
    if "yylogin" in driver.get_url():
        # 打开暗门
        for i in range(11):
            driver.click('//p[@class="split-line"]')
        # 输入账号
        driver.send_keys('//input[@placeholder="手机号"]', '18696832089')
        # 点击登录
        driver.click('//button[text()="登录后门"]')
    elif "contacts" in driver.get_url():
        pass


def test_click_login_trial(driver):
    # 打开网址
    driver.get('https://www1.transtalent.cn/')
    driver.click('//a[@id="login"]')
    driver.get_url()

def test_click_login_saleskit(driver):
    # 打开网址
    driver.get('https://www1.transtalent.cn/')
    driver.click('//div[@id="experience"]')
    driver.get_url()

def test_click_login_broadcast(driver):
    # 打开网址
    driver.get('https://www1.transtalent.cn/')

def test_click_login_tool(driver):
    # 打开网址
    driver.get('https://www1.transtalent.cn/')

def test_click_login_enquiry(driver):
    # 打开网址
    driver.get('https://www1.transtalent.cn/')

