# -*- coding:utf-8 -*-
# Author : Longhai
from time import sleep
from config import conf_system


def yy(driver):
    # driver.click("//span[text()='{}']/../..".format(config.M2))   # 进入课程学习
    driver.click("(//div[@class='course-elem-card clearfix'])[1]")  # 点击视频
    # sleep(1)
    driver.click("//span[@class='pv-icon-btn-play pv-iconfont']")   # 播放视频
    sleep(1)
    driver.yy_speed()   # 快进视频
    sleep(4)
    # sleep(1)
    driver.click("//div[@class='common-back-btn-sight close-btn']")  # 退出视频
    sleep(1)

    driver.click("(//div[@class='course-elem-card clearfix'])[2]")  # 点击视频
    # sleep(0.5)
    # driver.click("//span[@class='pv-icon-btn-play pv-iconfont']")  # 播放视频
    # sleep(0.5)
    # driver.yy_speed()   # 快进视频
    # driver.click("//span[@class='pv-icon-btn-play pv-iconfont']")  # 退出视频
    # sleep(0.5)
    #
    # driver.click("(//div[@class='course-elem-card clearfix'])[3]")  # 点击视频
    # sleep(0.5)
    # driver.click("//span[@class='pv-icon-btn-play pv-iconfont']")  # 播放视频
    # sleep(0.5)
    # driver.yy_speed()  # 快进视频
    # driver.click("//span[@class='pv-icon-btn-play pv-iconfont']")  # 退出视频
    # sleep(0.5)



    # # 进入下一视频
    # driver.click("//div[text()='进入下一视频']")