"""
Set Comprehension

Set -> {1, 2, 3, 4, 5}
"""
numeros = {1, 2, 3, 4, 5}
numeros_dobrados = {n * 2 for n in numeros}
print(numeros_dobrados)

numeros = {x ** 2 for x in range(10)}
print(numeros)

# transformando para dicionario
numeros = {x: x ** 2 for x in range(10)}
print(numeros)

letras = {letra for letra in 'Gabriel Miranda'}
print(letras)