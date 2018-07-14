# coding: utf-8

from os import path, walk
from src.utils.io import read_file, read_yaml, write_file
from src.utils.format import yaml_to_json

def execute(arguments = {}):
    origin = arguments['origin']
    destination = arguments['destination']
    default_filename = arguments['default_filename']
    bar_type = arguments['bar_type']

    origin_file = ''
    directory_origin = ''

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
            destination_file += bar_type + default_filename
        else:
            destination_file = directory_origin + bar_type + default_filename

    result_data = {}
    for dirname, dirnames, filenames in walk(directory_origin):
        for filename in filenames:
            structure_file = path.join(dirname, filename).split(directory_origin)[1].lstrip('\\/"')
            list_structure_file = structure_file.split(bar_type)

            code = ''
            for name in list_structure_file:
                list_path = [x for x in list_structure_file if list_structure_file.index(x) < list_structure_file.index(name)]
                list_path_adjusted = str(list_path).replace(', ', '][')

                if name == filename:
                    object_name = '.'.join(name.split('.')[:-1])
                    type_name = name.replace(object_name, '')
                    path_file = dirname + bar_type + filename

                    file_content = '{}'
                    if type_name == '.yaml':
                        yaml_content = read_yaml(path_file)
                        file_content = yaml_to_json(yaml_content)
                    elif type_name == '.json':
                        file_content = read_file(path_file)

                    file_content_adjusted = file_content.replace('true', 'True').replace('false', 'False')

                    if list_path:
                        code += 'result_data' + list_path_adjusted + '.update({\'' + object_name + '\': ' + file_content_adjusted + '})'
                    else:
                        code += 'result_data' + '.update({\'' + object_name + '\': ' + file_content_adjusted + '})'

                    eval(code)

                else:
                    if list_path:
                        code += 'result_data' + list_path_adjusted + '.update({\'' + name + '\': {}}),'
                    else:
                        code += 'result_data' + '.update({\'' + name + '\': {}}),'
    
    write_file(destination_file, str(result_data))
    
    return 'Mounted specification.'