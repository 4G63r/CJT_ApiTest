#!/usr/bin/env python
# -*-coding:utf-8 -*-

# @Author: songxiao
# @Time: 2019-09-27 01:14

import pytest


# @pytest.mark.parametrize(
#     "test_input, expected",
#     [
#         ("3+5", 8),
#         ("5+7", 12),
#         ("9/3", 3),
#         ("6*9", 42)
#     ]
# )
# def test_eval(test_input, expected):
#     print("______测试用例_______")
#     assert eval(test_input) == expected

@pytest.mark.parametrize(
    'url,data', [('www.a', '111'), ('www.b', '222'),('www.c', '333')]
)
def test_01(url, data):
    print(url,data)


if __name__ == '__main__':
    pytest.main(["-s", "aaaaa.py"])
