#!/usr/bin/env python
# -*-coding:utf-8 -*-

# @Author: songxiao
# @Time: 2019-09-25 15:25

import pytest
from common.login import Login

login = Login()


@pytest.fixture(scope='session')
def session():
    return login.session


@pytest.fixture(scope='session')
def url():
    return login.url
