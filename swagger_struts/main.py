# coding: utf-8

from os import path
from sys import modules

from swagger_struts.utils.util import get_bar_type

def execute(command = '', origin = '', destination = ''):
    response = None

    default_command = 'new'
    default_filename = 'swagger_struts.yaml'
    name_object_root = 'root_swagger_struts'
    bar_type = get_bar_type()

    path_commands = path.dirname(__file__) + bar_type + 'commands' + bar_type
    path_import_commands = 'swagger_struts.commands.' 
    extension_file_command = '.py'

    if command is '':
        file_command = path_commands + default_command + extension_file_command
        file_module_command = path_import_commands + default_command
    else:
        file_command = path_commands + command + extension_file_command
        file_module_command = path_import_commands + command

    if path.isfile(file_command):
        exec('import %s' % file_module_command)
        module_command = modules[file_module_command]
        
        object_command = {
            'origin': origin,
            'destination': destination,
            'default_filename': default_filename,
            'bar_type': bar_type,
            'name_object_root': name_object_root
        }

        response = module_command.execute(object_command)
    else:
        response = 'Invalid command. Use the --help or -h option to have more information.'

    return response