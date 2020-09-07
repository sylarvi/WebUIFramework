# -*-coding:utf-8 -*-
"""
Created on: 2020-06-23
@author: lixiao
"""

import configparser
import os.path
import time
from selenium import webdriver
from Logs.Logger import Logger

logger = Logger(logger='BrowserEngine').getlog()


class BrowserEngine:
    """
    封装webdriver类
    """
    dir = os.path.dirname(os.path.abspath('.'))  # 获取绝对路径
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_driver_path = dir + '/tools/IEDriverServer.exe'
    firfox_driver_path = dir + '/tools/geckodriver.exe'

    def __init__(self):
        self.driver = None

    def open_browser(self):
        config = configparser.ConfigParser()
        init_file_path = os.path.dirname(os.path.abspath('.')) + '/Config/config.ini'
        config.read(init_file_path, encoding='utf-8')

        browser = config.get('BrowserType', 'ChromeBrowser')
        logger.info('当前选择测试的浏览器为：%s', browser)
        url = config.get('TestUrl', 'url')
        logger.info('当前选择测试的url地址为：%s', url)

        if browser == 'Firfox':
            self.driver = webdriver.Firefox(self.firfox_driver_path)
            logger.info('Starting Firfox Browser Now')
        elif browser == 'IE':
            self.driver = webdriver.Ie(self.ie_driver_path)
            logger.info('Starting IE Browser Now')
        elif browser == 'Chrome':
            self.driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info('Starting Chrome Browser Now')

        self.driver.get(url)
        self.driver.maximize_window()
        logger.info("Maximize The Current Window.")
        self.driver.implicitly_wait(5)
        logger.info("Set Implicitly Wait 5s.")
        return self.driver


if __name__ == "__main__":
    test = BrowserEngine()
    test.open_browser()
    time.sleep(3)



