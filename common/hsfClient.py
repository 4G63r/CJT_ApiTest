#!/usr/bin/env python
# -*-coding:utf-8 -*-

# @Author: songxiao
# @Time: 2019-09-24 18:11

import requests
import unittest
import jsonpath


class BodyType:
    URL_ENCODE = 1
    FORM = 2
    XML = 3
    JSON = 4
    FILE = 5


class HSFClient(unittest.TestCase):
    connect = None

    def __init__(self, url, method='GET', body_type=0, params=None):
        self.url = url
        self.method = method
        self.headers = {}
        self.body_type = body_type
        self.body = {}
        self.params = params
        self.res = None
        self._type_equality_funcs = {}

    def set_headers(self, headers):
        """设置请求头，参数为字典格式"""
        if isinstance(headers, dict):
            self.headers = headers
        else:
            raise TypeError('头信息请以字典格式传递')

    def set_header(self, key, value):
        """设置多个请求头时使用"""
        self.headers[key] = value

    def set_body(self, body):
        """设置请求体，参数为字典格式"""
        if isinstance(body, dict):
            self.body = body
        else:
            raise TypeError('正文内容请以字典格式传递，xml正文格式如下：{"xml": xml字符串}')

    def send(self):
        """发送请求"""
        self.method = self.method.upper().strip()
        if self.method == 'GET':
            self.res = requests.get(url=self.url, headers=self.headers, params=self.params)
        elif self.method == 'POST':
            if self.body_type == 1:
                self.set_header('Content-Type', 'application/x-www-form-urlencoded')
                self.res = requests.post(url=self.url, headers=self.headers, data=self.body)
            elif self.body_type == 2:
                self.res = requests.post(url=self.url, headers=self.headers, data=self.body)
            elif self.body_type == 3:
                self.set_header('Content-Type', 'text/xml')
                xml = self.body.get('xml')
                self.res = requests.post(url=self.url, headers=self.headers, data=xml)
            elif self.body_type == 4:
                self.set_header('Content-Type', 'application/json')
                self.res = requests.post(url=self.url, headers=self.headers, json=self.body)
            elif self.body_type == 5:
                self.res = requests.post(url=self.url, headers=self.headers, files=self.body)
            elif self.body_type == 0:
                self.res = requests.post(url=self.url, headers=self.headers)
            else:
                raise ValueError('正文格式类型参数错误')
        else:
            raise TypeError('请求方法类型错误，只支持get和post')

    @property
    def status_code(self):
        """响应状态码"""
        if self.res:
            return self.res.status_code
        else:
            return None

    @property
    def response_time(self):
        """响应时间(毫秒)"""
        if self.res:
            return round(self.res.elapsed.total_seconds() * 1000)
        else:
            return None

    @property
    def text(self):
        """响应正文内容"""
        if self.res:
            return self.res.text
        else:
            return None

    def response_to_json(self):
        """响应转为json对象"""
        if self.res:
            return self.res.json()
        else:
            return None

    def check_status_code_is(self, status_code):
        self.assertEqual(self.status_code, status_code, '响应状态码不是 %d' % status_code)

    def check_status_code_is_200(self):
        self.assertEqual(self.status_code, 200, '响应状态码不是 200')

    def check_response_time_less_than(self, duration=200):
        self.assertLess(self.response_time, duration, '响应时间超过%dms' % duration)

    def check_json_value(self, key, exp):
        if self.response_to_json():
            first = self.response_to_json().get(key)
        else:
            first = None
        self.assertEqual(first, exp, '值检查失败！实际结果：{} 预期结果：{}'.format(first, exp))

    def check_json_value_by_path(self, path, exp):
        if self.response_to_json():
            first = jsonpath.jsonpath(self.response_to_json(), path)
            if first == False:
                first = None
        else:
            first = None
        self.assertEqual(first, exp, '值检查失败！实际结果：{} 预期结果：{}'.format(first, exp))

    def check_db(self, sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        self.connect.commit()
        return cursor.fetchone()

    def log(self, msg):
        print(msg)
