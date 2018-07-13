# coding: utf-8

from os import path

from scripts.util import get_bar_type
from scripts.io import read_file, write_file

def execute(origin = '', destination = ''):
    bar = get_bar_type()
    default_filename = 'swagger_struts.yaml'

    origin_file = ''
    directory_origin = ''
    destination_file = default_filename

    if path.isfile(origin):
        origin_file = origin
        directory_origin = path.dirname(origin)
    else:
        origin_adjusted = origin.rstrip('\\/"')
        if path.isdir(origin_adjusted):
            directory_origin = origin_adjusted

    if not path.isfile(destination):
        destination_file = destination.rstrip('\\/"')
        if path.isdir(destination_file):
            destination_file += bar + default_filename
        else:
            destination_file = directory_origin + bar + default_filename
    
    origin_data = read_file(origin_file)

    write_file(destination_file, origin_data)

    # TODO: Escrever arquivo observando a estrutura do diretório.