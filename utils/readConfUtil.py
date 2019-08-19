#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-19 15:38

import configparser


class ReadConf:
    """读取ini配置文件"""

    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = conf_abspath
        else:
            self.file_path = file_path
        self.read_ini = self.get_read_ini()

    def get_read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path)
        return read_ini

    def get_ini_value(self, section, option):
        """
        获取配置文件中的value
        :param section:
        :param option:
        :return:
        """
        try:
            value = self.read_ini.get(section, option)
        except (configparser.NoSectionError, configparser.NoOptionError):
            value = None
        return value

    def get_value_list(self, section=None):
        if section is None:
            section = 'dingtalk'
        try:
            access_tokens = []
            options = self.read_ini.options(section)
            options = [i for i in options if 'access_token' in i]
            for option in options:
                at = self.get_ini_value(section, option)
                access_tokens.append(at)
            return access_tokens
        except configparser.NoSectionError:
            return None
