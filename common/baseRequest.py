#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-19 16:41

import requests
import urllib3


def base_request(method, url, headers=None, data=None, timeout=6, verify=False):
    """
    send a request

    :param method: 请求方法 get/post/put/delete
    :param url: 请求地址url
    :param headers: 请求头(optional) Dictionary
    :param data: 请求体(optional) Dictionary
    :param timeout: 超时时间(optional)
    :param verify: SSL认证(optional)
    :return: Response对象
    """
    urllib3.disable_warnings()
    try:
        if method.upper() == 'GET':
            res = requests.get(url, params=data, headers=headers, timeout=timeout, verify=verify)
        elif method.upper() == 'POST':
            res = requests.post(url, json=data, headers=headers, timeout=timeout, verify=verify)
        elif method.upper() == 'PUT':
            res = requests.put(url, json=data, headers=headers, timeout=timeout, verify=verify)
        elif method.upper() == 'DELETE':
            res = requests.delete(url, json=data, headers=headers, timeout=timeout, verify=verify)
        else:
            res = None
    except AttributeError:
        raise AttributeError
    else:
        return res


def session_(method, url, headers=None, data=None, timeout=6, verify=False):
    """
    send a request for creating a session

    :param method: 请求方法 get/post/put/delete
    :param url: 请求地址url
    :param headers: 请求头(optional) Dictionary
    :param data: 请求体(optional) Dictionary
    :param timeout: 超时时间(optional)
    :param verify: SSL认证(optional)
    :return: Session对象
    """
    s = requests.Session()
    s.headers = headers
    try:
        if method.upper() == 'GET':
            s.get(url, params=data, timeout=timeout, verify=verify)
        elif method.upper() == 'POST':
            s.post(url, json=data, timeout=timeout, verify=verify)
        elif method.upper() == 'PUT':
            s.put(url, json=data, timeout=timeout, verify=verify)
        elif method.upper() == 'DELETE':
            s.delete(url, json=data, timeout=timeout, verify=verify)
        else:
            s = None
    except AttributeError:
        raise AttributeError
    else:
        return s
