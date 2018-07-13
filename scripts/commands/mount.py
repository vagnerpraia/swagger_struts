# coding: utf-8

from os import path, walk
from scripts.utils.io import read_file, write_file

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
    
    origin_data = read_file(origin_file)
    write_file(destination_file, origin_data)

    result_data = {}
    for dirname, dirnames, filenames in walk(directory_origin):
        for filename in filenames:
            structure_file = path.join(dirname, filename).split(directory_origin)[1].lstrip('\\/"')
            list_structure_file = structure_file.split(bar_type)

            for name in list_structure_file:
                if name == filename:
                    print(name)
                    # TODO: Montar objeto.

    return 'Mounted specification.'