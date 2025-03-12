"""
Levantando os próprios erros com raise

raise -> Lança exceções

OBS: O raise não é uma função é uma palavra reservada, assim como def, ou qualquer outra em Python.

Para simplificar, pense no raise como sendo útil para que possamos criar nossas prórpias exceções e mensagens de erro.

A forma geral de utilização é:
raise TipoDoErro('Mensagem de erro')

#Ex Real

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string.')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string.')
    printf(f'O texto {texto} será impresso na cor {cor}')

colore('True', 7)

#Ex parecido

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string.')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string.')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    printf(f'O texto {texto} será impresso na cor {cor}')


colore('True', 7)

OBS: Nada após o raise é executado.
"""