"""
Listas aninhadas (Nested Lists)

- Arrays:
    - Unidimensionais (Arrays/Vetores)
    - Multidimensionais (Matrizes)

Em Python nós temos as listas que desempenham esse papel 
"""
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 x 3
print(listas)

# podemos acessar os dados da seguinte forma
print(listas[0])
print(listas[0][1]) # 2
print(listas[2][1]) # 8

print()
# iterando com loops em uma lista aninhada
for lista in listas:
    for numero in lista:
        print(numero, end=' ')
    print()

print()
# List Comprehension
[[print(valor) for valor in lista] for lista in listas]

print()
# Gerando tabuleiro
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)