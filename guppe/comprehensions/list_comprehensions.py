"""
List Comprehension (Compreensão de listas)

Utilizando List Comprehension, nós podfemos gerar novsas listas com dados processados a partir de outro iterável

# Sintaxe da List Comprehension:
[ dado for dado in iteravel ]
"""
# Exemplos
numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]
print(res)

"""
Podemos dividir a expressão em duas partes:

-> for numero in numeros
-> numero * 10

Para cada número na lista de números faça a expressão (numero * 10)
"""
res = [numero / 2 for numero in numeros]
print(res)

def funcao(valor):
    return valor ** 2

res = [funcao(numero) for numero in numeros]
print(res)

# List Comprehension X Loop
# Loop
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

for numero in numeros:
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados)

# List Comprehension
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = [numero * 2 for numero in numeros]

print(numeros_dobrados)

# Outros exemplos
nome = 'Geek University'
print([letra.upper() for letra in nome])

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print([amigo.title() for amigo in amigos])

print([numero * 3 for numero in range(1, 11)])

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

print([str(numero) for numero in [1, 2, 3, 4, 5]])

"""
Nós podemos adicionar estruturas condicionais lógicas às nossas List Comprehensions
"""
numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impares)

# Refatorar
# Qualquer número par módulo de 2 é 0, 0 em Python é False, logo not False = True
pares = [numero for numero in numeros if not numero % 2]

# Qualquer número ímpar módulo de 2 é 1, 1 em Python é True
impares = [numero for numero in numeros if numero % 2]
print(pares)
print(impares)

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)
