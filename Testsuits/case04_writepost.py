# -*-coding:utf-8 -*-
"""
Created on: 2020-06-23
@author: lixiao
"""

import time
import unittest
from Framework.BasePage import BasePage
from Logs.Logger import Logger

logger = Logger(logger='Writepost').getlog()


class WritePost(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = BasePage()
        logger.info('开始执行测试用例')

    def test01_post(self):
        """
        把测试用例逻辑代码封装到一个test开头的方法里
        """
        self.driver.click('xpath', '//*[@id="internationalHeader"]/div[1]/div/div[3]/div[2]/div[1]/div/span/div/span')
        self.driver.switch_window()
        pageurl = self.driver.get_url()
        self.driver.implicitly_wait(3)
        self.driver.click('xpath', '//*[@id="geetest-wrap"]/div/div[1]/span[2]')
        self.driver.implicitly_wait(2)
        tel_number = '18713102271'
        verify_number = '981079'
        self.driver.input('xpath', '//*[@id="geetest-wrap"]/div/div[3]/div[1]/div/input', tel_number)
        logger.info('输入登录手机号为：%s' % tel_number)
        time.sleep(3)
        self.driver.input('xpath', '//*[@id="geetest-wrap"]/div/div[3]/div[3]/div/input', verify_number)
        logger.info('输入登录验证码为：%s' % verify_number)
        time.sleep(3)
        self.driver.click('xpath', '//*[@id="geetest-wrap"]/div/div[5]/a[1]')
        logger.info('点击登录按钮')
        time.sleep(7)

    def test02_writepost(self):
        self.driver.click('xpath', '//*[@id="internationalHeader"]/div[1]/div/div[3]/div[2]/div[4]/div/div/a/span')
        time.sleep(5)
        self.driver.input('xpath', '//*[@id="editor"]', 'have a good day')
        logger.info('完成动态内容输入')
        self.driver.implicitly_wait(2)
        self.driver.click('xpath',
                          '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/button')
        time.sleep(3)
        self.driver.click('xpath',
                          '#app > div > div.home-page.f-clear > div.home-container > div > div.center-panel > div.section-block > div > div > div.toolbar > div.toolbar-box > div.bp-emoji-box-container.toolbar-item > div > div > div.content-ctnr > div.emoji-page.ps.ps--active-y > ul > li:nth-child(4) > div')
        logger.info('完成动态表情插入')
        time.sleep(3)
        self.driver.click('xpath', '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[2]/button')
        logger.info('点击发布动态按钮')
        time.sleep(3)
        content = self.driver.get_text('xpath',
                                       '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div/div/div/div')
        self.assertEqual('have a good day', content)
        time.sleep(3)
        self.driver.click('css_selector',
                          '#app > div > div.home-page.f-clear > div.home-container > div > div.center-panel > div.card-list > div.feed-card > div.content > div:nth-child(1) > div.button-area.c-pointer > div')
        self.driver.implicitly_wait(5)
        self.driver.click('xpath', '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/p')
        time.sleep(3)
        self.driver.click('xpath', '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/button[1]/span')
        pagesource = self.driver.pagesource()
        self.assertIn(content, pagesource)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        logger.info('结束执行测试用例')


if __name__ == '__main__':
    unittest.main()
