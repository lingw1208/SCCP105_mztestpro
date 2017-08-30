# __author__ = 'Ztiny'
# -*-coding:utf-8-*-

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from base import Page
from time import sleep

class login(Page):
    """
    用户登录界面
    """

    url = '/'

    #Action

    login_username_loc = (By.ID, 'username')

    login_password_loc = (By.ID, 'password')

    login_button_loc = (By.ID, "commonLog")

    #登录用户名
    def login_username(self, username):
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)

    #登录密码
    def login_password(self, password):
        self.find_element(*self.login_password_loc).clear()
        self.find_element(*self.login_password_loc).send_keys(password)

    #登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    #统一登录入口
    def user_login(self, username="", password=""):
        '''获取用户名和面登录'''
        self.open()
        #self.sccp_login()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(2)

    user_error_hint_loc = (By.ID, "msg")
    pawd_error_hint_loc = (By.ID, "msg")
    user_login_success_loc = (By.XPATH, ".//*[@id='personCenter']/span")

    #用户名错误提示
    def user_error_hint(self):
        return self.find_element(*self.user_error_hint_loc).text

    #密码错误提示
    def pawd_error_hint(self):
        return self.find_element(*self.pawd_error_hint_loc).text

    #登录成功用户名
    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text