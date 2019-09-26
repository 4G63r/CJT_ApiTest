#!/usr/bin/env python
# -*-coding:utf-8 -*-

# @Author: lina
# @Time: 2019-09-25 22:51


class Step:
    def __init__(self):
        self.step_name = ''  # 步骤名称
        self.step_desc = ''  # 步骤描述
        self.api = ''  # 接口名称或接口信息（包含接口名称、请求类型get或post、headers等信息的json串）
        self.input = ''  # 接口输入
        self.vars = []  # 中间变量保存赋值表达式，用于上下接口之间的数据依赖
        self.asserts = []  # 断言
