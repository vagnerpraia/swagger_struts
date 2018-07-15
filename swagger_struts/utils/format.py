# coding: utf-8

from json import dumps

def yaml_to_json(data):
    data = dumps(data)

    return data