#!/usr/bin/env python
# -*-coding:utf-8 -*-

# @Author: lina
# @Time: 2019-09-25 22:51


class Case:
    def __init__(self):
        self.case_name = ''  # 用例名称
        self.case_desc = ''  # 用例描述
        self.vars = []  # 变量赋值表达式
        self.steps = []  # 用例步骤
