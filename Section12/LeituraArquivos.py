"""
Leitura de arquivos

Para ler o conteúdo de um arquivo em Python, utilizamos a função integrada open(), que literalmente significa 'abrir'.

open() -> Na forma mais simples de utilização, nós passamos apenas um parâmetro de entrada, 
que neste caso é o nome do arquivo a ser lido. Essa função retorna um _io.TextIOWrapper 
e é com ele que trabalhamos então.

# OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve existir, ou então teremos o erro FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='UTF-8'>

mode='r' -> Modo de leitura. Este é o padrão.

# Exemplo
arquivo = open('texto.txt')

print(arquivo)
print(type(arquivo))

"""

# Exemplo
try:
    arquivo = open('texto.txt')
    print(arquivo)
    print(type(arquivo))
except FileNotFoundError:
    print("Arquivo não encontrado")