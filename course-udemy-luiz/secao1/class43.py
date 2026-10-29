"""
Cuidados com dados mutáveis
- copiado o valor (imutáveis)
- aponta para o mesmo valor a memória (mutável)

# nome = 'Luiz'
# outra = nome
# nome = 'João'
# print(nome)
# print(outra)
"""
# Shallow Copy (Cópia Rasa)
lista_a = ['Luiz', 'Maria']
lista_b = lista_a
# apontam para o mesmo espaço de memória, logo a
# alteração vai para as duas listas
lista_b.append('Gustavo')

print(lista_a)
print(lista_b)

# Deep Copy (Cópia Profunda)
lista_a = ['Luiz', 'Maria']
lista_b = lista_a.copy()

lista_b.append('Gustavo')

print(lista_a)
print(lista_b)