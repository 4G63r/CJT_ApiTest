#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-23 16:12


def assert_status_code(res):
    if res.status_code == 200:
        return True
    else:
        return False
