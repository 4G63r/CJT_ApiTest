#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-19 16:04

from utils.readConfUtil import ReadConfUtil

r = ReadConfUtil()


def get_test_host():
    return r.get_conf_value('test_host', 'addr')


def get_inte_host():
    return r.get_conf_value('inte_host', 'addr')


def get_host_addr():
    """
    获取host地址
    :return: https://inte-cloud.chanjet.com/cc/0000/0
    """
    env_mode = r.get_conf_value('env_mode', 'mode')
    app_name = r.get_conf_value('app_name', 'name')
    if env_mode.upper() == 'TEST':
        return get_test_host().replace('app_name', app_name)
    elif env_mode.upper() == 'INTE':
        return get_inte_host().replace('app_name', app_name)
    else:
        raise Exception('env_mode配置错误!!!')


def get_account_info():
    """获取用户账密"""
    un = r.get_conf_value('account', 'username')
    pw = r.get_conf_value('account', 'password')
    return {'username': un, 'password': pw}
