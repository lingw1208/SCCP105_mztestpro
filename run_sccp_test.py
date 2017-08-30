# coding=utf-8
from email.header import Header

from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
import smtplib
import unittest
import time
import os, sys

reload(sys)
sys.setdefaultencoding("utf-8")

"""
# =========================邮件接收者============================
mailto_list=["lingwei@fablesoft.cn"]
#============= 设置服务器，用户名、口令以及邮箱的后缀===============
mail_host="smtp.mail126.com"
mail_user="13770336439@mail126.com"
mail_pass="lingwei456"
"""
# ===========================发送邮件============================
def send_mail(file_new):

        # to_list:发给谁
        # sub:主题
        # content:内容
        # send_mail("aaa@126.com","sub","content")

    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("portal登录自动化测试报告", "utf-8")

    smtp = smtplib.SMTP()
    smtp.connect("smtp.exmail.qq.com")
    smtp.login("lingwei@fablesoft.cn", "Lingwei123")
    smtp.sendmail("lingwei@fablesoft.cn", "672057954@qq.com", msg.as_string())
    smtp.quit()
    print "email has send out"

# ==============查找测试报告目录，找到最新生成的测试报告文件==========
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getatime("./sccp/report/" + "\\" + fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':
    #test_portal = "./sccp/report/"
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './sccp/report/' + now +'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='portal登录自动化测试报告',
                            description='环境 ：window 7 浏览器：firefox')
    discover = unittest.defaultTestLoader.discover('./sccp/test_case', pattern='*_sta.py')
    runner.run(discover)
    fp.close()
    file_path = new_report("./sccp/report/")

    #send_mail(file_path)