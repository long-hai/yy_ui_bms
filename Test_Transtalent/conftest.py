# -*- coding:utf-8 -*-
# Author : Longhai
import time

import pytest
from tools.ui.base_ui import BaseUI


@pytest.fixture(scope='session')
def driver():
    base = BaseUI()
    # 打开浏览器
    base.start_browser("mobile")
    # 登录
    base.get("http://m-uat.transtalent.cn/new-login")
    base.click('//span[text()="使用账号登录 >"]')
    base.send_keys('//input[@placeholder="请输入账号"]', 'lh20')
    base.send_keys('//input[@placeholder="请输入密码"]', '20')
    base.click('//button')
    time.sleep(2)
    yield base
