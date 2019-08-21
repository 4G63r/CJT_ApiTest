#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-19 16:04

from utils.readConfUtil import ReadConfUtil
from utils.MD5_encode import md5_encode

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
    app_name = r.get_conf_value('app_name', 'name').lower()
    if env_mode.upper() == 'TEST':
        return get_test_host().replace('app_name', app_name)
    elif env_mode.upper() == 'INTE':
        return get_inte_host().replace('app_name', app_name)
    else:
        raise Exception('env_mode配置错误!!!')


def get_account_info():
    """
    获取用户账密
    如果平台是WEB端，密码需要MD5加密处理
    :return:
    """
    platform_name = get_platform()
    un = r.get_conf_value('account', 'username')
    pw = r.get_conf_value('account', 'password')

    if platform_name == 'APP':
        return {'username': un, 'password': pw}
    elif platform_name == 'WEB':
        return {'username': un, 'password': md5_encode(pw)}
    else:
        return


def get_platform():
    """获取平台名称 - web/app"""
    return r.get_conf_value('platform', 'name').upper()


def get_web_uid():
    return r.get_conf_value('web', 'uid')


def get_web_auth():
    return r.get_conf_value('web', 'auth')
