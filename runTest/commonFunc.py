# -*- coding: utf-8 -*-
import json
import jsonpath


def get(a, b):
    return a + b


def get_by_json_path(json_str, json_path):
    json_str = str(json_str)
    json_str = json_str.replace("'", "\"")
    jsonobj = json.loads(json_str)
    return jsonpath.jsonpath(jsonobj, json_path)
