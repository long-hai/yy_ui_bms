# -*- coding:utf-8 -*-
# Author : Longhai
from time import sleep
from config import conf_system


def before(driver):
    sleep(1)
    driver.click("//span[text()='{}']/../..".format(conf_system.M1))
    driver.click("//div[text()='进入能力诊断']")
    sleep(0.5)
    driver.click("(//div[text()='下一步'])[1]")
    sleep(0.5)
    driver.click("//div[text()='我知道啦']")
    # 获取前测题目数量
    bq_num = driver.get_text("(//span[@class='bold'])[1]")
    if len(bq_num) == 5:
        bq_num = int((str(bq_num))[3:4])
    else:
        bq_num = int((str(bq_num))[3:5])
    for i in range(bq_num):
        # 最有效措施
        driver.click("(//p[text()='最有效措施']/..)[{}]".format(i+1))
        # # 最有效措施-选择A
        driver.click("(//div[@class='effectiveOption']/div)[{}]".format(2+(i*5)))
        # # 最无效措施
        driver.click("(//p[text()='最无效措施']/..)[{}]".format(i+1))
        # # 最无效措施-选择D
        driver.click("(//div[@class='invalidOption']/div)[{}]".format(5+(i*5)))
        # 查看结果
        if i == bq_num-1:
            # 前测查看结果按钮
            driver.click("(//span[text()='查看结果']/..)")
            # 前测查看报告按钮
            driver.click("//div[text()='查看报告']")
            # 退出到课程模块
            driver.click("(//div[@class='common-back-btn-sight closeBtn'])[2]")
            break
        # 进入下一题
        driver.click("(//span[text()='下一题']/..)[{}]".format(i+1))
        # sleep(0.5)
        # 情景二:下一步
        if i == (bq_num/2)-1:
            driver.click("(//div[text()='下一步'])[2]")
            sleep(2)

