# coding: utf-8

import sys
from src import main

if len(sys.argv) == 2 and sys.argv[1] in ['--help', '-h']:
    namefile = '.'.join(__file__.split('.')[:-1])

    print('Usage: py ' + namefile + ' [options] [arguments]')

    print('\nOptions:')
    print('  -h, --help                 print this help message')

    print('\nArguments:')
    print('  argument 1 (optional)     address of the source file or directory')
    print('  argument 2 (optional)     address of the destination file or directory')
    
    print('\nDocumentation can be found at https://github.com/vagnerpraia/swagger_struts/')

elif len(sys.argv) == 1:
    main.execute()
    
elif len(sys.argv) == 2:
    main.execute(sys.argv[1])
    
elif len(sys.argv) == 3:
    main.execute(sys.argv[1], sys.argv[2])
    
else:
    print('Invalid command. Use the -help or -h option to have more information.')