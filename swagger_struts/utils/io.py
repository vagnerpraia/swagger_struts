# coding: utf-8

from os import path
from yaml import safe_load

def read_file(file):
    data = ''

    if path.isfile(file):
        with open(file, 'r', encoding = 'utf-8') as f:
            data = f.read()

    return data

def read_yaml(file):
    data = ''
    
    with open(file, 'r', encoding = 'utf-8') as f:
        data = safe_load(f)

    return data

def write_file(file, data):
    with open(file, 'w', encoding = 'utf-8') as f:
        f.write(data)

def append_file(file, data):
    with open(file, 'a', encoding = 'utf-8') as f:
        f.write(data)