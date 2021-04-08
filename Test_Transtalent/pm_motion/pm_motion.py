import time


# 首页进入课程
def into_course(driver, c_name):
    # 点击课程
    driver.click("//div[text()='{}']".format(c_name))
    time.sleep(1)
# 进入能力诊断
def into_diagnose(driver):
    driver.click("//span[text()='能力诊断']/..")

# 进入课程学习
def into_learning(driver):
    driver.click("//span[text()='课程学习']/..")

# 进入情景模拟
def into_scene(driver):
    driver.click("//span[text()='情景模拟']/..")
    driver.click("//div[@class='practiceList-listeImgItemHead-Img']")
    time.sleep(1)

# 退出情景模拟
def out_scene(driver):
    driver.click("//div[@class='common-back-btn-sight']")


# 进入能力考核
def into_assess(driver):
    driver.click("//span[text()='能力考核']/..")
