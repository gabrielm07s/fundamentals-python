"""
Sorted
Não confunda com a função sort(), o sort() só funciona em Listas

Podemos utilizar sorted() com qualquer iterável
Sorted serve para ordenar elementos
"""
tupla = (10, 298, 38, 34, 35, 21, 1)
conjunto = {10, 298, 38, 34, 35, 21, 1}
dicionario = {1: 10, 2: 298, 3: 38, 4: 34, 5: 35, 6: 21, 7: 1}

print(f'Tupla Original: {tupla}')
print(f'Tupla Ordenada: {sorted(tupla)}')
print(f'Conjunto Original: {conjunto}')
print(f'Conjunto Ordenado: {sorted(conjunto)}')
print(f'Dicionário Original: {dicionario}')
print(f'Dicionário Ordenado: {sorted(dicionario.values())}')

# sorted() não modifica, ele retorna uma nova lista, a lista original se mantém intacta 
# sempre retornar uma lista com os elementos do iterável ordenados

# Adicionando parâmetros ao sorted
numeros = (6, 1, 8 ,2)
print(sorted(numeros))
print(sorted(numeros, reverse=True)) # ordena do maior pra o menor

# Podemos usar sorted() para situações mais complexas
usuarios = [
    { "username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    { "username": "carla", "tweets": ["Eu amo meu gato"]},
    { "username": "jeff", "tweets": []},
    { "username": "bob123", "tweets": [], "cor": "amarelo"},
    { "username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    { "username": "gal", "tweets": [], "cor": "preto", "musica": "rock"},
]

print(usuarios)
# ORDENANDO em ORDEM ALFABÉTICA
print(sorted(usuarios, key=lambda usuario: usuario["username"], reverse=False))

# ORDENANDO pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too young to die", "tocou": 32},
]

# Ordenando da menos tocada pra mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordenando da mais tocada pra menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))

