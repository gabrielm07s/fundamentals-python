lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b # estendendo lista_a e lista_b na lista_c
print(lista_c)

# extend não retorna nada, retorna None, não te entrega 
# nada
lista_d = []
lista_d.extend(lista_a)
print(lista_a)