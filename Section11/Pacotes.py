"""
Pacotes

Módulo -> É apenas um arquivo Python que pode ter diversas funções para utilizarmos.
Pacote -> É um diretório contendo uma coleção de módulos.

OBS: Nas versões 2.x do Python, um pacote Python deveria conter dentro dele um arquivo chamado __init__.py

Nas versões 3.x do Python, um pacote Python é um diretório que DEVE conter um arquivo chamado __init__.py

OBS: Nas versões 3.x, não é mais obrigatória a utilização do arquivo __init__.py, mas normalmente ainda é utilizado para manter a compatibilidade.


"""

from geek import geek1, geek2
from geek.university import geek3, geek4