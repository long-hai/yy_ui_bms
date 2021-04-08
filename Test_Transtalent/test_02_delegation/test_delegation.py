"""
0 qf  4  jl   1  wln  3  fkk  gl  2
//div[@class="fontSize18 lineHeight32 nameBox3"]
//div[@class="fontSize18 notSelectedBtn"]
"""
import time
from test_m_transtalent.pm_motion import pm_motion
from test_m_transtalent.test_02m_delegation import pm_delegation


class Test_Delegation():

    def test_home(self, driver):
        pm_motion.into_course(driver, "授权")     # 进入课程

    def test_scene(self, driver):
        pm_motion.into_scene(driver)    # 进入情景模拟
        pm_delegation.delegation_vido(driver)  # 播放视频
        driver.click("//div[@id='startBtn']")   # 开始任务
        time.sleep(1)
        # 3  3  3  4  3
        for i in range(21):
            driver.click_location(1, 1)
            time.sleep(1)
        driver.click("//div[@class='portraitCircle portraitCircle2']")
        driver.click("//div[@class='fontSize18 selectedBtn']")
        driver.click("//div[@id='analysisBtn']")
        for i in range(10):
            # driver.click("//div[@id='choice1']")
            driver.click("//div[@id='choice2']")
            driver.click("//span[text()='看看我选对了吗']")
            driver.click("//span[text()='下一句']")
            time.sleep(1)
        driver.click("//span[text()='进入讨论准备表']")
        driver.click("//div[contains(text(),'找高朗，准备授权')]")
        driver.click("//div[@id='wrap']")
