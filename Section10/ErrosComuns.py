"""
Erros mais comuns em Python

Erros mais comuns: 
1 - SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que o Python não reconhece como parte da linguagem.

Ex a)

def funcao:
    print('Geek University')

    
b) def = 1

c) return

2 - NameError -> Ocorre quando uma variável ou função  ão foi definida
Ex
a)
print(geek)

b)
geek()

3 - TypeError - Ocorre quando uma função/operação/ação é aplicada a um tipo errado
Ex
a)
print(len(5))

b)
print('Geek' + [])

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando o índice inválido.
Ex
a)
lista = ['Geek']
print(lista[2])

b)
tupla = ('Geek')
print(tupla[0][10])

5 - ValueError -> Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto mas valor inapropriado.
Ex
a)
print(int('Geek'))

6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.
Ex
a)
dic = {'geek': 'university'}
print(dic['geek'])

7 - AtributeError -> Ocorre quando uma variavel não tem um atrbuto/função
Ex
a)
tupla = (12, 2, 31, 4)
print(tupla.sort())

8 - IndentationError -> Ocorre quando  ão respeitamos a indentação do Python (4 Espaços)
Ex
a)
def nova():
print('Geek')

OBS: Exceptions e Erros são sinônimos na programação.
"""