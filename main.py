#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-21 13:43

from common.login import Login
from business.warehouse import WarehouseBusiness
from business.custvendor import CustVendor

login = Login()
front_url = login.url
s = login.session
