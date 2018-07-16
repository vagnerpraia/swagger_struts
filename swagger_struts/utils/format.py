# coding: utf-8

from json import dumps
from yaml import dump, load

def yaml_to_json(data):
    formatted_data = dumps(data)

    return formatted_data

def json_to_yaml(data):
    formatted_data = dump(load(data), allow_unicode = True, default_flow_style = False)

    return formatted_data