# coding: utf-8

import platform

def get_bar_type():
    separator = '/'

    if platform.system() is 'Windows':
        separator = '\\'
    
    return separator