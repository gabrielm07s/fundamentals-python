"""
Função lambda Python
A função lambda é uma função como outra no Python, porém estas são funções anônimas
que contêm apenas uma linha, ou seja, tudo deve ser contido dentro de uma única expressão
"""
lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# lista = [4, 32, 1, 34, 5, 6, 6, 21]
# lista.sort(reverse=True)

# lista.sort(key=lambda item: item['nome']) # cria copia rasa
# print(lista)

lista_ordenada = sorted(lista, key=lambda item: item['nome'])
print(lista_ordenada)