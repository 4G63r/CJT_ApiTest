#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-23 16:12


def assert_status_code(res, status_code):
    if res.status_code == status_code:
        return True
    else:
        return False
