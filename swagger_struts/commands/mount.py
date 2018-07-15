# coding: utf-8

from os import path, walk
from swagger_struts.utils.io import read_file, read_yaml, write_file
from swagger_struts.utils.format import yaml_to_json

def execute(arguments = {}):
    origin = arguments['origin']
    destination = arguments['destination']
    default_filename = arguments['default_filename']
    bar_type = arguments['bar_type']
    name_object_root = arguments['name_object_root']

    origin_file = ''
    origin_directory = ''

    if path.isfile(origin):
        origin_file = origin
        origin_directory = path.dirname(origin)
    else:
        origin_adjusted = origin.rstrip('\\/"')
        if path.isdir(origin_adjusted):
            origin_directory = origin_adjusted

    destination_file = destination.rstrip('\\/"')
    destination_directory_adjusted = bar_type.join(destination_file.split(bar_type)[:-1])

    if path.isdir(destination_file):
        destination_file += bar_type + default_filename
    else:
        if not path.isdir(destination_directory_adjusted):
            destination_file = origin_directory + bar_type + default_filename
    
    result_data = {}
    for directory_name, directory_names, filenames in walk(origin_directory):
        for filename in filenames:
            structure_file = path.join(directory_name, filename).split(origin_directory)[1].lstrip('\\/"')
            list_structure_file = structure_file.split(bar_type)

            code = ''
            for name in list_structure_file:
                list_path = [x for x in list_structure_file if list_structure_file.index(x) < list_structure_file.index(name)]
                list_path_adjusted = str(list_path).replace(', ', '][')

                if name == filename:
                    object_name = '.'.join(name.split('.')[:-1])
                    type_name = name.replace(object_name, '')
                    path_file = directory_name + bar_type + filename

                    file_content = '{}'
                    if type_name == '.yaml':
                        yaml_content = read_yaml(path_file)
                        file_content = yaml_to_json(yaml_content)
                    elif type_name == '.json':
                        file_content = read_file(path_file)

                    file_content_adjusted = file_content.replace('true', 'True').replace('false', 'False')

                    if (directory_name + bar_type + filename) == origin_file:
                        object_name = name_object_root

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
    
    result_data_adjusted = str(result_data)\
        .replace('\'', '"')\
        .replace('True', 'true')\
        .replace('False', 'false')\
        .replace('{"' + name_object_root + '": ', '')\

    result_data_adjusted = result_data_adjusted[:-1]

    write_file(destination_file, result_data_adjusted)
    
    return 'Mounted specification.'