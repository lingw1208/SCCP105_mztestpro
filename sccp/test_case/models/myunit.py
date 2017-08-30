# __author__ = 'Ztiny'
#-*-coding:utf-8-*-
from selenium import webdriver
from driver import browser
import unittest
import os
import time

# 定义MyTest()类用于继承unittest.TestCase类，因为后面所穿建的测试类中setUp()和teaeDown()方法所做的事情相同，
# 所以，将它们抽象为MyTest(0类，好处就是在编写测试用例时不再考虑这两个方法的实现
class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
