"""
Min e Max

max() - retorna o maior valor em um iterável ou o maior de dois ou mais elementos
min() - retorna o menor valor em um iterável ou o menor de dois ou mais elementos
"""
print('MAX')
lista = [1, 8, 4, 99, 34, 129]
tupla = (1, 8, 4, 99, 34, 129)
conjunto = {1, 8, 4, 99, 34, 129}
dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(lista)) # 129
print(max(tupla)) # 129
print(max(conjunto)) # 129
print(max(dicionario.values())) # 129

print(max(3, 34)) # 34
print(max(3, 34, 54)) # 54

print('\nMIN')
lista = [1, 8, 4, 99, 34, 129]
tupla = (1, 8, 4, 99, 34, 129)
conjunto = {1, 8, 4, 99, 34, 129}
dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(lista)) # 1
print(min(tupla)) # 1
print(min(conjunto)) # 1
print(min(dicionario.values())) # 1

print(min(3, 34)) # 3
print(min(3, 34, 54)) # 3

print('\nOutros exemplos:')
nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

# por padrão, ordem alfabética
print(max(nomes)) # Tim
print(min(nomes)) # Arya

# pelo tambanho
print(max(nomes, key=lambda nome: len(nome))) # Ollivander
print(min(nomes, key=lambda nome: len(nome))) # Tim
