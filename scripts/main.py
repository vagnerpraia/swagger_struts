# coding: utf-8

from os import getcwd, listdir, path

from scripts.utils.util import get_bar_type
from scripts.utils.io import read_file, write_file

def execute(command = '', origin = '', destination = ''):
    bar = get_bar_type()
    default_command = 'new'
    default_filename = 'swagger_struts.yaml'

    path_commands = path.dirname(__file__) + bar + 'commands'
    list_commands = ['.'.join(x.split('.')[:-1]) for x in listdir(path_commands)]
    
    if command not in list_commands:
        return None

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