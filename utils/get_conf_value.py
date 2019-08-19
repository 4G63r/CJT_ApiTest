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
    """获取host地址"""
    env = r.get_conf_value('host_addr', 'addr')
    if env.upper() == 'TEST':
        return get_test_host()
    elif env.upper() == 'INTE':
        return get_inte_host()
    else:
        raise Exception('env参数错误!!!')


def get_account_info():
    """获取用户账密"""
    un = r.get_conf_value('account', 'username')
    pw = r.get_conf_value('account', 'password')
    return {'username': un, 'password': pw}
