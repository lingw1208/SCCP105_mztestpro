# __author__ = 'Ztiny'
# -*-coding:utf-8-*-

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from base import Page
from time import sleep
import time
from loginPage import login

class xinjian(Page):
    """
    软件新建页面
    """

    url = '/'

    # Action
    ziguanli_loc = (By.XPATH, 'html/body/div[1]/div[1]/div[2]/ul/li[6]/a')
    zichanguanli_loc = (By.XPATH, ".//*[@id='menu']/div[3]/div[1]")
    xinjian_loc = (By.XPATH, "html/body/div[1]/div[3]/div/div/div[1]/table/tbody/tr/td/a/span/span")

    # 弹出软件新建窗口
    def dakaiziyuan(self, username='admin', password='123456'):
        login(self.driver).user_login(username, password)
        self.implicitly_wait(10)
        self.find_element(*self.ziguanli_loc).click()  # 资源管理
        time.implicitly_wait(10)
        self.switch_to.frame("component_1")
        sleep(5)
        self.find_element(*self.zichanguanli_loc).click() # 点击软件资产管理
        sleep(3)
        self.switch_to.default_content()
        self.switch_to.frame("component_2")
        self.find_element(*self.xinjian_loc).click()  # 点击新建

    ruanjian_loc = (By.ID, "ipt_title")

    #软件名称
    def ruanjian(self, rjmc):
        self.find_element(*self.rjmc_loc).clear()
        self.find_element(*self.rjmc_loc).send_keys(rjmc)