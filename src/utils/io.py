# coding: utf-8

from os import path
from json import dumps
from yaml import safe_load

def read_file(file):
    data = ''

    if path.isfile(file):
        with open(file, 'r') as f:
            data = f.read()

    return data

def read_yaml(file):
    with open(file, 'r', encoding='utf-8') as stream:
        yaml_data = safe_load(stream)

    data = dumps(yaml_data)

    return data

def write_file(file, data):
    with open(file, 'w') as f:
        f.write(data)

def append_file(file, data):
    with open(file, 'a') as f:
        f.write(data)