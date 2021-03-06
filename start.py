# coding: utf-8

from sys import path, argv
from os import getcwd

path.append(getcwd())

from swagger_struts.main import execute

responde = ''

if len(argv) == 2 and argv[1] in ['--help', '-h']:
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

elif len(argv) == 1:
    responde = execute()
    
elif len(argv) == 2:
    responde = execute(argv[1])
    
elif len(argv) == 3:
    responde = execute(argv[1], argv[2])
    
elif len(argv) == 4:
    responde = execute(argv[1], argv[2], argv[3])

else:
    responde = 'Invalid command. Use the --help or -h option to have more information.'

print('\n' + str(responde) + '\n')