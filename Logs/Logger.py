# -*-coding:utf-8 -*-
"""
Created on: 2020-06-23
@author: lixiao
"""

import logging
import time
import os.path


class Logger:
    def __init__(self, logger):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志保存到指定的文件中
        """
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        self.path = (os.path.dirname(os.getcwd() + '\\logs\\'))

        # 创建一个handler,用于写入日志文件
        log_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
        # print(log_time)
        # log_path = 'C:\\Users\\Administrator\\PycharmProjects\\HybridDrive-Framework\\Logs\\'
        log_path = os.path.dirname(os.path.abspath('.')) + '/logs/'
        log_name = log_path + log_time + '.log'
        # print(log_name)
        f_handler = logging.FileHandler(log_name, encoding='utf-8')
        f_handler.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        s_handler = logging.StreamHandler()
        s_handler.setLevel(logging.INFO)

        # 定义handler的输出格式
        output_format = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(name)s - %(levelname)s - '
                                          '%(message)s')
        f_handler.setFormatter(output_format)
        s_handler.setFormatter(output_format)

        # 给logger添加handler
        self.logger.addHandler(f_handler)
        self.logger.addHandler(s_handler)

    def getlog(self):
        return self.logger


if __name__ == '__main__':
    # logger = Logger(logger='test_log').getlog()
    # logger.info('打开浏览器')
    # logger.info('最大化浏览器窗口')
    # logger.info('打开首页')
    # logger.info('静置一秒')
    # logger.info('关闭并退出浏览器')
    print(os.getcwd())
    # 根目录
    print(os.path.dirname(os.getcwd()))
    # C:\Users\Administrator\PycharmProjects\HybridDrive - Framework
    # log_path = (os.path.dirname(os.getcwd())+ '\\Logs\\')
    log_path = os.getcwd() + '\\Logs\\'
    print(log_path)





