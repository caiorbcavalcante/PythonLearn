"""
O block try/except 

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo assim que o programa pare de funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    // Execução problemática
except:
    // O que deve ser feito em caso de problema

# Exemplo 1 - Tratando um erro genérico

try:
    geek()
except:
    print('Deu algum problema')
# Tentando executar a função geek(), caso nao consiga imprima a mensagem de erro.

OBS: Tratar erro de forma genérica não é a melhor forma de tratamento de erro. O ideal é SEMPRE tratar de forma específica.

# Exemplo 2 -  Tratando um erro específico

try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')

# Exemplo 3 -  Tratando um erro específico

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# Exemplo 4 - Podemos fazer vários tipos de blocos para verificar diferentes tipos de erro.

# Exemplo 5 - Em funções

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except ValueError:
        return None
    
dic {"nome": "Geek"}

print(pega_valor(dic, "nome"))

"""

   
