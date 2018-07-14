# coding: utf-8

from os import path
import yaml
def read_file(file):
    data = ''

    if path.isfile(file):
        with open(file, 'r') as f:
            data = f.read()

    return data

def read_yaml(file):
    print()
    print(file)
    print()
    yaml_file = read_file(file)
    data = yaml.load(yaml_file)
    return data

def write_file(file, data):
    with open(file, 'w') as f:
        f.write(data)

def append_file(file, data):
    with open(file, 'a') as f:
        f.write(data)