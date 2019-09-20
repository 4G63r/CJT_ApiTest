#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-19 16:04

from utils.readConfUtil import ReadConfUtil

r = ReadConfUtil()


def get_test_host():
    """
    test环境host
    :return: https://test-cloud.chanjet.com/app_name/0000/0
    """
    return r.get_conf_value('HOST', 'test')


def get_inte_host():
    """
    inte环境host
    :return: https://inte-cloud.chanjet.com/app_name/0000/0
    """
    return r.get_conf_value('HOST', 'inte')


def get_host_addr():
    """
    获取host地址
    :return: https://inte-cloud.chanjet.com/cc/0000/0
    """
    env_mode = r.get_conf_value('TEST_ENV', 'env')
    app_name = r.get_conf_value('APP_NAME', 'name').lower()
    if env_mode.upper() == 'TEST':
        return get_test_host().replace('app_name', app_name)
    elif env_mode.upper() == 'INTE':
        return get_inte_host().replace('app_name', app_name)
    else:
        raise Exception('<TEST_ENV>配置错误!!!')


def get_account_info():
    """
    获取用户账号密码
    :return:
    """
    username = r.get_conf_value('ACCOUNT', 'username')
    password = r.get_conf_value('ACCOUNT', 'password')
    return {'username': username, 'password': password}


def get_platform():
    """
    获取平台名称
    :return: WEB / APP
    """
    return r.get_conf_value('PLATFORM_NAME', 'name').upper()
