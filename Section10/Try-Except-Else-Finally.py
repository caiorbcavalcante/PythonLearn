"""
Try / Except / Else / Finally

Dica de quando e onde tratar código

TODA ENTRADA DEVE SER TRATADA:

OBS: A função do usuário é DESTRUIR seu sistema.

# Else - > É executado somente se não ocorrer o erro.
num = 0

try:
    num = int(input("Informe um número: "))
except ValueError:
    print("Valor incorreto")
else:
    print(f"Você digitou {num}")

# Finally

try:
    num = int(input("Informe um número: "))
except ValueError:
    print("Você não digitou um valor válido.")
else:
    print(f"Você digitou o número {num}")
finally:
    print("Executando o finally")

# OBS: O bloco finall é SEMPRE executado. Independente se houve exceção ou não.

# O finally, geralmente, é utilizado para fechar ou desalocar recursos.

# Exemplos mais complexos ERRADO

def dividir(a, b):
    return a / b

num1 = int(input("Informe o primeiro número: "))
try:
    num2 = int(input("Informe o primeiro número: "))
except ValueError:
    print("O valor precisa ser númerico")

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')

# Exemplos mais complexos CORRETO

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível dividir por 0'

n1 = int(input(''))
n2 = int(input(''))

print(dividir(n1, n2))

# Exemplos mais complexos - Semi Genérico

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

n1 = int(input(''))
n2 = int(input(''))

print(dividir(n1, n2))
"""


