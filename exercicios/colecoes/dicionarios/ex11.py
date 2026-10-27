"""
Dada uma lista de nomes e uma de idades, monte um dicionário com zip.
"""
nomes = ['Gabriel', 'Giovanna', 'Guilherme', 'Juliana']
idades = [19, 19, 12, 48]

dicionario = dict(zip(nomes, idades))
print(dicionario)