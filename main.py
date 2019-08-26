#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-21 13:43

from common.login import Login
from common import assertion
# from business.warehouse import WarehouseBusiness
# from business.custvendor import CustVendor
# from business.goods import Goods
from business.jhdReceipt import JhdReceipt

login = Login()
front_url = login.url
s = login.session

# c = CustVendor(front_url, s)
# g = Goods(front_url, s)

j = JhdReceipt(front_url, s, assertion)
j.create_jhd()
