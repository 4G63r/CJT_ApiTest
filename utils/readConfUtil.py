#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-19 15:38

import os
import configparser

cur_path = os.path.abspath(os.path.dirname(__file__))
conf_path = '%s/config.ini' % cur_path.replace('utils', 'conf')


class ReadConfUtil:
    """读取配置文件"""

    def __init__(self, file_path=None):
        if file_path is None:
            self.__file_path = conf_path
        else:
            self.__file_path = file_path
        self.__read_ini = self.__read_conf()

    def __read_conf(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.__file_path)
        return read_ini

    def get_conf_value(self, section, option):
        try:
            value = self.__read_ini.get(section, option)
        except (configparser.NoSectionError, configparser.NoOptionError):
            value = None
        return value

    def __get_test_host(self):
        """
        test环境host
        :return: https://test-cloud.chanjet.com/app_name/0000/0
        """
        return self.get_conf_value('HOST', 'test')

    def __get_inte_host(self):
        """
        inte环境host
        :return: https://inte-cloud.chanjet.com/app_name/0000/0
        """
        return self.get_conf_value('HOST', 'inte')

    @property
    def host_addr(self):
        """
        获取host地址
        :return: https://inte-cloud.chanjet.com/cc/0000/0
        """
        env_mode = self.get_conf_value('TEST_ENV', 'env')
        app_name = self.get_conf_value('APP_NAME', 'name').lower()
        if env_mode.upper() == 'TEST':
            return self.__get_test_host().replace('app_name', app_name)
        elif env_mode.upper() == 'INTE':
            return self.__get_inte_host().replace('app_name', app_name)
        else:
            raise Exception('<TEST_ENV>配置错误!!!')

    @property
    def account_info(self):
        """
        获取用户账号密码
        :return:
        """
        username = self.get_conf_value('ACCOUNT', 'username')
        password = self.get_conf_value('ACCOUNT', 'password')
        return {'username': username, 'password': password}

    @property
    def platform(self):
        """
        获取平台名称
        :return: WEB / APP
        """
        return self.get_conf_value('PLATFORM_NAME', 'name').upper()
