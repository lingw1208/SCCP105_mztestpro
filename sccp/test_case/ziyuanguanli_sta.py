# coding=utf-8

import random
import sys
import unittest
from time import sleep

#reload(sys)
#sys.setdefaultencoding("utf-8")

sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.loginPage import login
from page_obj.ziyuanPage import xinjian

#@unittest.skip("直接跳过测试")
class loginTest2(myunit.MyTest):
    """软件新建"""

    def user_login_verify(self, username='', password=''):
        xinjian(self.driver).dakaiziyuan(username, password)


    def test_login4(self):
        '''打开新建页'''
        self.user_login_verify(username='admin',password='123456')
        po = login(self.driver)
        self.assertEqual(po.user_login_success(), u"个人应用中心")
        function.insert_img(self.driver, u"用户名、密码正确.jpg")

if __name__ == '__main__':
    unittest.main()