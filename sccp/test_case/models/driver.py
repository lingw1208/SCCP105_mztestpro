# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

#启动浏览器驱动
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    time.sleep(1)
    return driver


"""
#用于测试该脚本是否有效
if __name__ == '__main__':
    dr = browser()
    dr.get("http://www.baidu.com")
    dr.quit()
"""
