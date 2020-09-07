# -*-coding:utf-8 -*-
"""
Created on: 2020-06-23
@author: lixiao
"""

import time
import unittest
from Framework.BasePage import BasePage
from Logs.Logger import Logger

logger = Logger(logger='Loginpage').getlog()


class HomePageSwitch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = BasePage()
        logger.info('开始执行测试用例')

    def test01_loginpage(self):
        """
        把测试用例逻辑代码封装到一个test开头的方法里
        """
        self.driver.click('xpath', '//*[@id="internationalHeader"]/div[1]/div/div[3]/div[2]/div[1]/div/span/div/span')
        self.driver.switch_window()
        title = self.driver.get_page_title()
        logger.info('获取当前页面标题：%s' % title)
        pageurl = self.driver.get_url()
        logger.info('获取当前页面url：%s' % pageurl)
        self.driver.implicitly_wait(3)
        assertstr = '登录'
        text = self.driver.get_text('class_name', 'tit')
        self.assertEqual(assertstr, text)

    def test02_faillogin(self):
        self.driver.click('xpath', '//*[@id="geetest-wrap"]/div/div[1]/span[2]')
        self.driver.implicitly_wait(2)
        tel_number = '13100000000'
        verify_number = '615337'
        self.driver.input('xpath', '//*[@id="geetest-wrap"]/div/div[3]/div[1]/div/input', tel_number)
        logger.info('输入登录手机号为：%s' % tel_number)
        time.sleep(3)
        self.driver.input('xpath', '//*[@id="geetest-wrap"]/div/div[3]/div[3]/div/input', verify_number)
        logger.info('输入登录验证码为：%s' % verify_number)
        time.sleep(3)
        self.driver.click('xpath', '//*[@id="geetest-wrap"]/div/div[5]/a[1]')
        logger.info('点击登录按钮')
        time.sleep(3)
        logininfo = self.driver.get_text('xpath', '//*[@id="geetest-wrap"]/div/div[3]/div[4]/p')
        print(logininfo)
        self.assertEqual('短信验证码已过期,请重新获取', logininfo)
        logger.info('验证码错误登录失败')

    def test03_passlogin(self):
        '//*[@id="geetest-wrap"]/div/div[3]/div[1]/div/input'
        self.driver.clear('xpath', '//*[@id="geetest-wrap"]/div/div[3]/div[1]/div/input')
        logger.info('已清除登录手机号文本框内容')
        time.sleep(2)
        self.driver.clear('xpath', '//*[@id="geetest-wrap"]/div/div[3]/div[3]/div/input')
        logger.info('已清除登录验证码文本框内容')
        time.sleep(2)
        tel_number = '18713102271'
        verify_number = '291899'
        self.driver.input('xpath', '//*[@id="geetest-wrap"]/div/div[3]/div[1]/div/input', tel_number)
        logger.info('输入登录手机号为：%s' % tel_number)
        time.sleep(2)
        self.driver.input('xpath', '//*[@id="geetest-wrap"]/div/div[3]/div[3]/div/input', verify_number)
        logger.info('输入登录验证码为：%s' % verify_number)
        time.sleep(2)
        self.driver.click('xpath', '//*[@id="geetest-wrap"]/div/div[5]/a[1]')
        logger.info('点击登录按钮')
        time.sleep(3)
        text = self.driver.get_text('xpath', '//*[@id="internationalHeader"]/div[1]/div/div[3]/div[2]/div[3]/div/div[1]/a/span')
        self.assertEqual('消息', text)
        logger.info('登录成功')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        logger.info('结束执行测试用例')


if __name__ == '__main__':
    unittest.main()