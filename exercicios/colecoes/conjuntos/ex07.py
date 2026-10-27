"""
Adicione um elemento novo com add() e depois adicione um que já existe. 
Imprima o conjunto após cada passo e comente o que aconteceu.
"""
conjunto = {3, 6, 9, 12}
print(conjunto)

conjunto.add(4)
print(conjunto)

conjunto.add(4) # adicionar um elemento existente é apenas ignorado
print(conjunto)