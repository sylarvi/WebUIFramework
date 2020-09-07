# -*-coding:utf-8 -*-
"""
Created on: 2020-06-23
@author: lixiao
"""

import unittest
import os
import time
from TestReport import HTMLTestRunner
from Email.Email_handle import SendEmail


# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '\\TestReport\\'
print('report_path' + report_path)

# 获取系统当前时间
now = time.strftime("%Y-%m-%d—_%H_%M_%S", time.localtime())

# 设置报告名称格式
HtmlFile = report_path + now + "Testreport.html"
fp = open(HtmlFile, "wb")

# case路径
case_path = os.path.dirname(os.path.abspath('.')) + 'Testsuits'
suite = unittest.TestLoader().discover(case_path, pattern="case*.py", top_level_dir=None)

if __name__ == '__main__':
    # 执行所有测试用例
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"UI自动化测试报告", description=u"用例测试情况")
    # 开始执行测试套件
    runner.run(suite)
    fp.close()
    SendEmail().send_email(HtmlFile)
