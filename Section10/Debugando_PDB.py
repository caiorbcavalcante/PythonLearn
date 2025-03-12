"""
Debugando com o PDB

PDB -> Python Debugger

"""

def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'DEU MERDA'

n1 = input("")
n2 = input("")
print(dividir(n1, n2))
