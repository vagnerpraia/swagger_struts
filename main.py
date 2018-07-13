# coding: utf-8

import sys
from startup import execute

if len(sys.argv) == 2 and sys.argv[1] == '--help':
    print('')
    print('O script aguarda os seguintes parâmetros:')
    print('')
    print('    Arquivo ou diretório de origem (Opcional): Endereço do arquivo ou diretório com a estrutura da especificação.')
    print('    Arquivo ou diretório de destino (Opcional): Endereço do arquivo ou diretório com o resultado padronizado da especificação.')
    print('\n')
    print('Notas:')
    print('')
    print('    * Não sendo passados os parâmetros, os endereços serão considerados o local do script.')
    print('    * Não sendo passados o parâmetro do arquivo ou diretório de destino, será considerado o diretório de origem também para o destino.')
    print('    * Não sendo especificado o nome considerados aos arquivos serão swagger-struts.yaml.')
    print('')
    
elif len(sys.argv) == 1:
    execute()
    
elif len(sys.argv) == 2:
    execute(sys.argv[1])
    
elif len(sys.argv) == 3:
    execute(sys.argv[1], sys.argv[2])
    
else:
    print('Comando inválido. Utilize o comando \'' + sys.argv[0] + ' help\' para ter mais informações.')