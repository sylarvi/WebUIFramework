# -*-coding:utf-8 -*-
"""
Created on: 2020-06-23
@author: lixiao
"""

import time
import os.path
from Logs.Logger import Logger
from selenium.webdriver.common.by import By
from Framework.BrowserEngine import BrowserEngine
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = Logger(logger='BasePage').getlog()


class BasePage:
    """
    封装封装selenium中的常用操作方法类
    """
    def __init__(self):
        self.locationTypeDict = {
            'id': By.ID,
            'name': By.NAME,
            'class_name': By.CLASS_NAME,
            'css_selector': By.CSS_SELECTOR,
            'tag_name': By.TAG_NAME,
            'xpath': By.XPATH,
            'link_text': By.LINK_TEXT,
            'partial_link_text': By.PARTIAL_LINK_TEXT
        }
        self.driver = BrowserEngine().open_browser()

    # 页面前进操作
    def forward(self):
        self.driver.forward()
        logger.info('Click Forward On Current Page')

    # 页面后退操作
    def back(self):
        self.driver.back()
        logger.info('Click Back On Current Page')

    # 页面刷新
    def refresh(self):
        self.refresh()
        logger.info('Refresh The Page')

    # 页面滚动
    def scroll(self, px1, px2):
        # window.scrollBy(0, 500)　　  向下滚动500个像素
        # window.scrollBy(0, -500)　　 向上滚动500个像素
        # window.scrollBy(500, 0)　　  向右滚动500个像素
        # window.scrollBy(-500, 0)　　 向左滚动500个像素
        bds = 'window.scrollBy({}, {})'.format(px1, px2)
        self.driver.execute_script(bds)
        logger.info('Page scroll successfully')

    # 获取页面源码
    def pagesource(self):
        pagesource = self.driver.page_source
        logger.info('Get Pagesource successfully')
        return pagesource

    # 获取当前页面url
    def get_url(self):
        pageurl = self.driver.current_url
        logger.info('get current_url successfully')
        return pageurl

    # 隐式等待
    def implicitly_wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info('implicitly wait %d s' % seconds)

    def find_element(self, locationType, locatorExpression):
        try:
            # print(self.locationTypeDict[locationType])
            if self.locationTypeDict[locationType]:
                # "显示等待页面元素出现在DOM中，不一定可见，存在则返回该页面元素对象"
                # element = self.driver(self.locationTypeDict[locationType], locatorExpression)
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(((self.locationTypeDict[locationType], locatorExpression))))
                return element
            else:
                logger.error('Locationtype error')
        except Exception as e:
            logger.error(e)

    # 弹出框操作
    def alert(self):
        self.driver.switch_to.alert()
        logger.info('switch to alert')

    def alert_text(self):
        return self.driver.switch_to.alert.text

    def alert_accept(self):
        self.driver.switch_to.alert.accept()
        logger.info('Accepted Alert')

    def alert_dismiss(self):
        self.driver.switch_to.alert.dismiss()
        logger.info('dismissed Alert')

    def alert_input(self, key):
        self.driver.switch_to.alert.send_keys(key)
        logger.info('Alert input %s' % key)

    # 关闭当前窗口
    def close_windows(self):
        try:
            self.driver.close()
            logger.info("Closing The Windows.")
        except NameError as e:
            logger.error("Failed to quit the browser with %s" % e)

    # 截图保存
    def get_screenshot(self):
        file_path = os.path.dirname(os.path.abspath('.')) + '/Screenshots/'
        file_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
        file_name = file_path + file_time + '.png'
        try:
            self.driver.get_screenshot_as_file(file_name)
            logger.info('Take screenshot and save to folder : /Screenshots')
        except Exception as e:
            logger.error('Failed to make screenshot! -- %s' % e)

    # 输入
    def input(self, locationType, expression, text):
        element = self.find_element(locationType, expression)
        print(element)
        try:
            element.send_keys(text)
            logger.info("Had input \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to input in inputbox with %s" % e)

    # 清除文本框
    def clear(self, locationType, expression):
        element = self.find_element(locationType, expression)
        try:
            element.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)

    # 点击元素
    def click(self, locationType, expression):
        time.sleep(2)
        element = self.find_element(locationType, expression)
        try:
            element.click()
            logger.info("The element was clicked.")
        except Exception as e:
            logger.error("Failed to click the element with %s" % e)

    # 获取网页标题
    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    # 获取文本内容
    def get_text(self, locationType, expression):
        text = self.find_element(locationType, expression).text
        logger.info("text is %s" % text)
        return text

    # 检查页面元素是否存在
    def check_element(self, val):
        result = self.driver.find_element_by_class_name(val)
        if len(result) == 1:
            return True
        return False

    # 切换跳转页
    def switch_window(self):
        n = self.driver.window_handles  # 获取当前页句柄
        self.driver.switch_to.window(n[1])  # 切换到新的网页窗口

    # 隐式菜单处理
    def implicit_menu(self):
        js = 'document.getElementsByClassName("van-popover van-popper van-popper-channel")[0].style.display = "block";'
        self.driver = self.driver.execute_script(js)
        time.sleep(3)
        self.click('css_selector','#van-popover-3593 > div > div > a:nth-child(1)')
        # van-popover-1171 > div > div > a:nth-child(1)
        # time.sleep(3)
        # self.click('xpath', '//*[@id="van-popover-8810"]/div/div/a[6]')

    # 关闭浏览器
    def quit(self):
        self.driver.quit()
        logger.info("The Browsre has closed")

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)


if __name__ == '__main__':
    driver = BasePage()
    print(driver)
    driver.input('class_name', 'nav-search-keyword', 'pytohn')
    time.sleep(3)
    driver.clear('class_name', 'nav-search-keyword')
    driver.scroll(0, 300)
    # driver.implicit_menu()
    # driver.click('xpath', '//*[@id="van-popover-8810"]/div/div/a[6]')