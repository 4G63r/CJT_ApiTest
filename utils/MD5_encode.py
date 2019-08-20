#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-20 10:30

import hashlib


def md5_encode(data):
    md5 = hashlib.md5()
    md5.update(data.encode(encoding="utf-8"))
    sign = md5.hexdigest()
    return sign
