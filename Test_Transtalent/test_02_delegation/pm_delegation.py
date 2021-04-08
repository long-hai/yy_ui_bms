import time

# 授权情景模拟前视频
def delegation_vido(driver):
    driver.switch_to_frame("//iframe[@name='polyvPlayer']")
    driver.click('//img[@id="playbutton"]')
    time.sleep(1)
    driver.click_location(159, 285)
    time.sleep(3)