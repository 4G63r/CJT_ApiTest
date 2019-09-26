#!/usr/bin/env python
# -*-coding:utf-8 -*-

# @Author: songxiao
# @Time: 2019-09-25 15:25

import pytest, requests

s = requests.session()


@pytest.fixture()
def login1():
    url = "https://xxxxx/global/do-login.action"
    body = {
        'loginName': '账号',
        'password': 111111,
        'pcCodeForFocusMedia': 0
    }
    data = s.post(url, data=body, verify=False)
    print(data.json())
