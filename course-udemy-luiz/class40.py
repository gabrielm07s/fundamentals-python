"""
Listas em Python
Suporta vários valores de qualquer tipo

Create  Read  Update   Delete
Criar   Ler   Alterar  Apagar 
"""
lista = [1, 2, 3, 4]
numero = lista[2] # acessando e pegando valores (READ)
lista[2] = 300 # alterando (atualizando) (UPDATE)
print(lista[2]) # acessando o índice dois

del lista[2] # apagando o índice dois da lista (DELETE)
print(lista)

lista.append(5) # adicionando ao final da lista o item 50
lista.append(6)
print(lista)

item_removido = lista.pop() # removendo o último elemento
# podemos guardar a váriavel, pois retorna o elemento removido (retorna)
print(lista, item_removido) 

item_removido = lista.pop(3)
print(lista, item_removido) # podemos remover itens com índice pelo pop também