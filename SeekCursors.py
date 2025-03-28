"""
Seek e Cursors

seek() -> É utilizado para movimentar o cursor pelo arquivo.

arquivo = open('texto.txt')
print(arquivo.read())

# Exemplo de seek()
arquivo = open('texto.txt')
print(arquivo.read())

# Movimentando o cursor pelo arquivo com a função seek()
arquivo.seek(0)

"""
# 1 - Abrir o arquivo
arquivo = open('texto.txt')
# 2 - Trabalhar com o arquivo
print(arquivo.read())

print(arquivo.closed()) # Verifica se o arquivo está fechado ou não
# 3 - Fechar o arquivo
arquivo.close() 

