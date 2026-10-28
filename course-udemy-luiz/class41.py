"""
append - adiciona um item ao final
insert - adiciona um item no índice escolhido
pop - remove do final ou do índice escolhido
del - apaga um índice
clear - limpa a lista
extend - estende a lista
+ - concatena lista
"""
lista = [10, 20, 30, 40]
# adicionando item
lista.append('Luiz')
print(lista)

# remover item
nome = lista.pop()
print(nome, lista)

lista.append(1233)
print(lista)

# deletando item
del lista[-1]
print(lista)

# limpa a lista
## lista.clear()
## print(lista)

# insert adiciona um item no índice passado no primeiro parâmetro
lista.insert(0, 'Valor')
print(lista)