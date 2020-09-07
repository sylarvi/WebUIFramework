# -*-coding:utf-8 -*-
"""
Created on: 2020-06-23
@author: lixiao
"""

import re
import time
import unittest
from Framework.BasePage import BasePage
from Logs.Logger import Logger

logger = Logger(logger='Homepage_Switch').getlog()


class HomePageSwitch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = BasePage()
        logger.info('开始执行测试用例')

    def test01_dougapage(self):
        """
        把测试用例逻辑代码封装到一个test开头的方法里
        """
        self.driver.click('css_selector', '#primaryChannelMenu>span:nth-child(1)>div.item.van-popover__reference>a>span')
        title = self.driver.get_page_title()
        logger.info('获取当前页面标题：%s' % title)
        pageurl = self.driver.get_url()
        logger.info('获取当前页面url：%s' % pageurl)
        self.driver.implicitly_wait(3)
        assertstr = 'MAD·AMV'
        text = self.driver.get_text('xpath', '//*[@id="subnav"]/ul/li[2]/a')
        self.assertEqual(assertstr, text)
        time.sleep(2)
        self.driver.back()

    def test02_musicpage(self):
        self.driver.implicitly_wait(5)
        self.driver.click('css_selector', '#primaryChannelMenu > span:nth-child(3) > div > a > span')
        pagetitle = self.driver.get_page_title()
        pattern = re.compile('(.*?)-哔哩哔哩', re.S)
        assertstr = pattern.findall(pagetitle)[0]
        logger.info('断言关键字：%s' % assertstr)
        self.assertEqual(assertstr, '音乐')


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        logger.info('结束执行测试用例')


if __name__ == '__main__':
    unittest.main()