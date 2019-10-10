#!/usr/bin/env python
# -*-coding:utf-8 -*-

# @Author: lina
# @Time: 2019-09-25 22:51

# import re
# import traceback
# import pytest
# from runTest import caseLoader
# from utils.logUtil import LogUtil
# from conf import filePath
# from Case import Case
# from utils import operaExcel
# from runTest import commonFunc
# from runTest import assertFunc

# logger = LogUtil()


class CaseRunner:
    def __init__(self, ):
        self.var_dict = {}
        # self.api_file_path = "data\\testdatas.xlsx"

#     def test_run_case(self, case_json_str):
#         case_result = True
#         try:
#             case = caseLoader.loadcase_from_json(case_json_str)
#             logging.info("开始执行用例：%s" % case.casename)
#             # 解析变量将变量和结果保存到全局字典
#             for var in case.vars:
#                 var_name, var_value = self.parse_var_expression(var, None)
#                 self.var_dict[var_name] = var_value
#             # 依次执行用例步骤
#             for step in case.steps:
#                 try:
#                     step_result = True
#                     logging.info("开始执行步骤：%s" % step.stepname)
#                     # 解析api和input，并调用执行api
#                     api_data = ExcelUtil.get_excel_data_by_key(self.api_file_path, step.api)
#                     if not api_data:
#                         logging.error("没有找到api配置信息，%s" % step.api)
#                         logging.error("执行步骤失败：%s" % step.stepname)
#                         return False
#                     api_data = self.parse(api_data, None)
#                     input_data = self.parse(step.input, None)
#                     logging.info("开始执行接口：%s，输入为：%s" % (step.api, input_data))
#                     response = self.run_api(api_data, input_data)
#                     logging.info("接口%s执行完毕，返回结果为：%s" % (step.api, response))
#                     # 解析变量将变量和结果保存到全局字典
#                     for var in step.vars:
#                         var_name, var_value = self.parse_var_expression(var, response)
#                         self.var_dict[var_name] = var_value
#                     for assert_item in step.asserts:
#                         actual = self.parse(assert_item['actual'], response)
#                         expect = self.parse(assert_item['expect'], response)
#                         # 反射执行assertname函数
#                         func_str = "AssertFunc.%s(actual,expect)" % (assert_item['assertname'])
#                         if not eval(func_str, {'actual': actual, 'expect': expect, 'AssertFunc': AssertFunc}):
#                             logging.error("执行断言失败：%s，期望：%s，实际：%s" % (assert_item, expect, actual))
#                             step_result = False
#                             case_result = False
#                             continue
#                         logging.info("执行断言成功：%s" % assert_item)
#                     if not step_result:
#                         logging.error("执行步骤失败：%s" % step.stepname)
#                         return False
#                     logging.info("执行步骤成功：%s" % step.stepname)
#                 except Exception as e:
#                     logging.error("执行步骤%s出现异常：%s" % (step.stepname, traceback.format_exc()))
#                     return False
#                 finally:
#                     logging.info("步骤%s执行后，中间变量结果为：%s" % (step.stepname, self.var_dict))
#             return case_result
#         except Exception as e:
#             logging.error("执行用例%s出现异常：%s" % (case.casename, traceback.format_exc()))
#             return False
#
#     # 解析变量表达式，得到变量名称和对应值
#     def parse_var_expression(self, var_expression, response):
#         if not "=" in var_expression:
#             raise ValueError("变量表达式格式不正确，请检查，%s" % var_expression)
#         var_name = var_expression.split("=")[0].strip()
#         var_value = self.parse(var_expression.split("=")[1].strip(), response)
#         return var_name, var_value
#
#     # 解析字符串表达式，替换里面的VAR变量和func函数，并计算表达式结果
#     def parse(self, expression, response):
#         expression = str(expression)
#         response = str(response)
#         # 正则匹配,替换变量
#         vars = re.findall(".*VAR\[(.*)\].*", expression)
#         for var in vars:
#             tmpstr = "VAR[%s]" % var
#             expression = expression.replace(tmpstr, self.var_dict.get(var))
#         # 正则匹配，替换函数,暂不支持func嵌套
#         funcs = re.findall(".*Func_(.*).*", expression)
#         for func in funcs:
#             tmpstr = "Func_%s" % func
#             expression = expression.replace(tmpstr, str(
#                 eval("CommonFunc.%s" % func, {'response': response, 'CommonFunc': CommonFunc})))
#         try:
#             return eval(expression)
#         except Exception as e:
#             return expression
#
#     # 执行api接口，api为接口信息的json串，input为接口输入
#     def run_api(self, api, input):
#         return "{'data':{'id':1,'name':'name1'}}"
#
#
# case_json_str = '''{
#     "casename": "用例名称",
#     "casedesc": "用例描述",
#     "vars": [
#         "name1=value1",
#         "name2=Func_get(1,2)"
#     ],
#     "steps": [
#         {
#             "stepname": "步骤1名称",
#             "stepdesc": "步骤1描述",
#             "api": "api1",
#             "input": {},
#             "vars": [
#                     "name3=Func_get_by_json_path(response,'$.data.id')",
#                     "name4=Func_get_by_json_path(response,'$.data.name')"
#             ],
#             "asserts": [
#                 {
#                     "actual": "VAR[name1]",
#                     "assertname": "assertEqual",
#                     "expect": "value1"
#                 },
#                 {
#                     "actual": "Func_get_by_json_path(response,'$.data.name')",
#                     "assertname": "assertEqual",
#                     "expect": "name1"
#                 }
#             ]
#         },
#         {
#             "stepname": "步骤2名称",
#             "stepdesc": "步骤2描述",
#             "api": "api2",
#             "input": {},
#             "vars": [
#                     "name3=Func_get_by_json_path(response,'$.data.id')",
#                     "name4=Func_get_by_json_path(response,'$.data.name')"
#             ],
#             "asserts": [
#                 {
#                     "actual": "Func_get_by_json_path(response,'$.data.id')",
#                     "assertname": "assertEqual",
#                     "expect": "1"
#                 },
#                 {
#                     "actual": "Func_get_by_json_path(response,'$.data.name')",
#                     "assertname": "assertEqual",
#                     "expect": "name"
#                 }
#             ]
#         }
#     ]
# }'''
# caseRunner = CaseRunner()
# caseRunner.run_case(case_json_str)
