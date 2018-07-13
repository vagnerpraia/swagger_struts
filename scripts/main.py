# coding: utf-8

from os import path
from sys import modules

from scripts.utils.util import get_bar_type
from scripts.utils.io import read_file, write_file

def execute(command = '', origin = '', destination = ''):
    bar = get_bar_type()
    default_command = 'new'
    default_filename = 'swagger_struts.yaml'

    path_commands = path.dirname(__file__) + bar + 'commands' + bar
    path_import_commands = 'scripts.commands.' 
    extension_file_command = '.py'

    if command is '':
        file_command = path_commands + default_command + extension_file_command
        command_execute = path_import_commands + default_command
    else:
        file_command = path_commands + command + extension_file_command
        command_execute = path_import_commands + command

    if path.isfile(file_command):
        __import__(command_execute)
        mymodule = modules[command_execute]
        print('Teste 1')
    else:
        return 'Invalid command. Use the --help or -h option to have more information.'

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