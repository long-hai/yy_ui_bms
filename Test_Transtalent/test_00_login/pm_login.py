from time import sleep


def m_login(driver):
    # 打开网址
    driver.get("http://m-uat.transtalent.cn/new-login")
    driver.click('//span[text()="使用账号登录 >"]')
    driver.send_keys('//input[@placeholder="请输入账号"]', 'lh20')
    driver.send_keys('//input[@placeholder="请输入密码"]', '20')
    driver.click('//button[@class="submitBtn_3 fontSize16 lineHeight24"]')
    sleep(2)