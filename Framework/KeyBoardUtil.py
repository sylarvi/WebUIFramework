# -*-coding:utf-8 -*-
"""
Created on: 2020-06-23
@author: lixiao
"""

import time
import win32api, win32con
from Framework.BrowserEngine import BrowserEngine


class KeyboardKeys:
    """封装模拟键盘按键类"""
    VK_CODE = {"enter": 13, "ctrl": 17, "tab": 9, 'backspace': 8, 'pageup': 33, 'pagedown': 34}

    @staticmethod
    def keyDown(keyName):
        # 按下按键
        win32api.keybd_event(KeyboardKeys.VK_CODE[keyName], 0, 0, 0)

    @staticmethod
    def keyUp(keyName):
        # 释放按键
        win32api.keybd_event(KeyboardKeys.VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)

    @staticmethod
    def oneKey(key):
        # 模拟单个按键
        KeyboardKeys.keyDown(key)
        KeyboardKeys.keyUp(key)

    @staticmethod
    def twoKeys(key1, key2):
        # 模拟两个组合键
        KeyboardKeys.keyDown(key1)
        KeyboardKeys.keyDown(key2)
        KeyboardKeys.keyUp(key1)
        KeyboardKeys.keyUp(key2)


if __name__ == "__main__":
    driver = BrowserEngine()
    time.sleep(2)
    KeyboardKeys().oneKey("pageup")

