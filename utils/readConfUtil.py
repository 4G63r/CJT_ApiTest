#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-19 15:38

import os
import configparser

cur_path = os.path.dirname(__file__)
conf_path = '%s/config.ini' % cur_path.replace('utils', 'conf')


class ReadConfUtil:
    """读取配置文件"""

    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = conf_path
        else:
            self.file_path = file_path
        self.read_ini = self.read_conf()

    def read_conf(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path)
        return read_ini

    def get_conf_value(self, section, option):
        """查询配置文件中的值"""
        try:
            value = self.read_ini.get(section, option)
        except (configparser.NoSectionError, configparser.NoOptionError):
            value = None
        return value
