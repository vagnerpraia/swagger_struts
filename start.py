# coding: utf-8

import sys
import os
sys.path.append(os.getcwd())

from scripts.main import execute

if len(sys.argv) == 2 and sys.argv[1] in ['--help', '-h']:
    namefile = '.'.join(__file__.split('.')[:-1])

    print('Usage: py ' + namefile + ' [options] [command] [arguments]')

    print('\nOptions:')
    print('  -h, --help         print this help message')

    print('\nCommands:')
    print('  new                create new project')
    print('  mount              mount project following the contents of the source files')

    print('\nArguments:')
    print('  argument 1         address of the source file or directory')
    print('  argument 2         address of the destination file or directory')
    
    print('\nDocumentation can be found at https://github.com/vagnerpraia/swagger_struts/')

elif len(sys.argv) == 1:
    execute()
    
elif len(sys.argv) == 2:
    execute(sys.argv[1])
    
elif len(sys.argv) == 3:
    execute(sys.argv[1], sys.argv[2])
    
else:
    print('Invalid command. Use the --help or -h option to have more information.')