# coding: utf-8

from os import path, walk
from swagger_struts.utils.io import read_file, read_yaml, write_file
from swagger_struts.utils.format import yaml_to_json, json_to_yaml

def execute(arguments = {}):
    origin = arguments['origin']
    destination = arguments['destination']
    default_filename = arguments['default_filename']
    bar_type = arguments['bar_type']

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
    list_code = []
    for directory_name, directory_names, filenames in walk(origin_directory):
        for filename in filenames:
            structure_file = path.join(directory_name, filename).split(origin_directory)[1].lstrip('\\/"')
            list_structure_file = structure_file.split(bar_type)

            for name in list_structure_file:
                list_path = [x for x in list_structure_file if list_structure_file.index(x) < list_structure_file.index(name)]
                list_path_adjusted = str(list_path).replace(', ', '][')
                flag_update_root = list_path_adjusted == '[]'

                code = ''
                if name == filename:
                    object_name = '.'.join(name.split('.')[:-1])
                    type_name = name.replace(object_name, '')
                    path_file = directory_name + bar_type + filename

                    file_content = ''
                    if type_name == '.yaml':
                        yaml_content = read_yaml(path_file)
                        file_content = yaml_to_json(yaml_content)
                    elif type_name == '.json':
                        json_content = read_file(path_file)
                        json_content_adjusted = json_content.replace('\n', '').replace('\t', '')
                        file_content = json_content_adjusted

                    if file_content:
                        file_content_adjusted = file_content.replace('true', 'True').replace('false', 'False')

                        if flag_update_root:
                            code = 'result_data.update(' + file_content_adjusted + ')'
                        else:
                            code = 'result_data' + list_path_adjusted + '.update({\'' + object_name + '\': ' + file_content_adjusted + '})'
                            
                else:
                    if flag_update_root:
                        code = 'result_data.update({\'' + name + '\': {}})'
                    else:
                        code = 'result_data' + list_path_adjusted + '.update({\'' + name + '\': {}})'
                        
                    
                if code and code not in list_code:
                    eval(code)                        
                    list_code.append(code)

    result_data_adjusted = str(result_data)\
        .replace('\'', '"')\
        .replace('True', 'true')\
        .replace('False', 'false')

    destination_type = destination_file.split('.')[-1]
    if destination_type == 'yaml':
        result_data_adjusted = json_to_yaml(result_data_adjusted)

    write_file(destination_file, result_data_adjusted)

    return 'Mounted specification.'