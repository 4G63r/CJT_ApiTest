#!/usr/bin/env python
# -*-coding:utf-8 -*-

# @Author: lina
# @Time: 2019-09-25 22:51

import json
from runTest.case import Case
from runTest.step import Step


# 将json格式用例转换成Case对象
def loadcase_from_json(case_json_str):
    try:
        obj = json.loads(case_json_str)
        case = Case()
        case.case_name = obj['casename']
        case.case_desc = obj['casedesc']
        case.vars = obj['vars']
        for tmp in obj['steps']:
            step = Step()
            step.step_name = tmp['stepname']
            step.step_desc = tmp['stepdesc']
            step.api = tmp['api']
            step.input = tmp['input']
            step.vars = tmp['vars']
            step.asserts = tmp['asserts']
            case.steps.append(step)
        return case
    except Exception as e:
        raise ValueError("解析用例json表达式出现异常,%s" % e)
