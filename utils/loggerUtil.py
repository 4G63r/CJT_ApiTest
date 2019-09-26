#!/usr/bin/env python
# -*-coding:utf-8 -*-

# @Author: songxiao
# @Time: 2019-09-24 20:09

import os
import logging
import logging.handlers as hd

cur_path = os.path.abspath(os.path.dirname(__file__))
log_path = cur_path.replace('utils', 'log')


class LoggerUtil:
    def __init__(self):
        self.logger = logging.getLogger("CJT_ApiTest")
        # 设置日志级别
        self.logger.setLevel(logging.INFO)
        # 日志内容输出格式设置
        # fmt = '%(asctime)s  %(filename)s  %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s'
        fmt = '%(asctime)s %(levelname)s %(message)s'
        datefmt = '%a, %d %b %Y %H:%M:%S'
        format = logging.Formatter(fmt, datefmt)
        # 输出日志到文件中
        handle_1 = hd.TimedRotatingFileHandler(log_path, backupCount=20, encoding="utf-8")
        handle_1.setFormatter(format)
        handle_1.setLevel(logging.INFO)
        # 输出日志到控制台
        hs = logging.StreamHandler()
        hs.setFormatter(format)
        hs.setLevel(logging.INFO)
        # 避免log重复
        if not self.logger.handlers:
            self.logger.addHandler(handle_1)
            self.logger.addHandler(hs)

    # 定义各日志级别
    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def error(self, msg):
        self.logger.error(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def critical(self, msg):
        self.logger.critical(msg)

    def exception(self, msg):
        self.logger.exception(msg)
