# Swagger Struts
Swagger Struts - Estruturador de documentação de API

## Utilização
A chamada da ferramenta segue a seguinte estrutura:
* py start.py [options] [command] [arguments]

A lista de comandos é a seguinte:
* new: Criar novo projeto de especificação de API.
* mount: Montar especificação de API seguindo a estrutura dos arquivos fontes.

A lista de argumentos é a seguinte:
* Arquivo ou diretório de origem (Opcional): Endereço do arquivo ou diretório com a estrutura da especificação.
* Arquivo ou diretório de destino (Opcional): Endereço do arquivo ou diretório com o resultado padronizado da especificação.

Notas:
* Todos os parâmetros são opcionais.
* Não sendo passado o comando, será considerado o comando new.
* Não sendo passados os parâmetros, os endereços serão considerados o local do script.
* Não sendo passados o parâmetro do arquivo ou diretório de destino, será considerado o diretório de origem também para o destino.
* Não sendo especificado o nome considerados aos arquivos serão swagger-struts.yaml.