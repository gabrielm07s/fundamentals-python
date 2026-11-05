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