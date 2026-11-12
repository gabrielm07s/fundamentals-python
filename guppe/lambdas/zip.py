"""
Zip

zip() - cria um iterável (Zip Object) que agrega elemento de cada um dos iteráveis passados como entrada em pares
"""
lista1 = [1, 2, 3]
lista2 = [4, 5 ,6]

zip1 = zip(lista1, lista2)
print(zip1, type(zip1))

print(list(zip(lista1, lista2)))
print(tuple(zip(lista1, lista2)))
print(set(zip(lista1, lista2)))
print(dict(zip(lista1, lista2)))

"""
O zip() utiliza como parâmetro o menor tamanho em iterável, isos significa que se estiver trabalhyando com
iteráveis de tamanhos diferentes ele irá parar quandoos elementos do menor iterável acabar
"""
lista3 = [7, 8, 9, 10]
print(list(zip(lista1, lista2, lista3)))

# podemos usar diferentes tipos de iteráveis com zip
tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

print(list(zip(tupla, lista, dicionario.values()))) 

# lista de tuplas
dados = [(0,1), (1,2), (2,3), (3,4), (4,5)]
print(list(zip(*dados)))

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))