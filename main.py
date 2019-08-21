#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-21 13:43

from common.login import Login
from business.warehouse import WarehouseBusiness

login = Login()
front_url = login.url
s = login.session

w = WarehouseBusiness(front_url, s)
print(w.get_warehouse_infos())
