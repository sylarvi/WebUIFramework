# -*-coding:utf-8 -*-
"""
Created on: 2020-06-23
@author: lixiao
"""

import time
import unittest
from Framework.BasePage import BasePage
from Logs.Logger import Logger

logger = Logger(logger='Homepage_search').getlog()

# homepage = Homepage()
# homepage.home_input('class_name', 'nav-search-keyword', 'pytohn')
# time.sleep(10)


class HomePageSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = BasePage()
        logger.info('开始执行测试用例')

    def test01_homepage(self):
        """
        把测试用例逻辑代码封装到一个test开头的方法里
        """
        title = self.driver.get_page_title()
        logger.info('获取当前页面标题：%s' % title)
        pageurl = self.driver.get_url()
        logger.info('获取当前页面url：%s' % pageurl)
        # print(title)
        try:
            self.assertIn('哔哩哔哩', title)
            self.assertEqual('https://www.bilibili.com/', pageurl)
        except Exception as e:
            logger.error(e)

    def test02_search(self):
        time.sleep(1)
        keyword = 'python'
        self.driver.input('class_name', 'nav-search-keyword', keyword)
        logger.info('输入框输入查询关键字：%s' % keyword)
        self.driver.implicitly_wait(3)
        self.driver.click('class_name', 'nav-search-btn')
        logger.info('点击搜索按钮')
        self.driver.implicitly_wait(5)
        self.driver.switch_window()
        logger.info('切换到新标签页')
        text = self.driver.get_text('xpath', '//*[@id="all-list"]/div[1]/div[1]/ul[1]/li[1]/a')
        # try:
        self.assertEqual('12', text)
        # except Exception as e:
        #     logger.error(e)
        self.driver.get_screenshot()

    def test03_scroll(self):
        self.driver.scroll(0, 500)
        logger.info('完成页面滑动操作')
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        logger.info('结束执行测试用例')


if __name__ == '__main__':
    unittest.main()
