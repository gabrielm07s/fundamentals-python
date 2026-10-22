"""
Palíndromo: diga se uma lista é igual à sua inversa ([1,2,3,2,1]).
"""
lista = [1, 2, 3, 2, 1]
lista_reserva = lista[::-1]

print(lista)
print(lista_reserva)
if lista == lista_reserva:
    print('É palíndromo')
else:
    print('Não é palíndromo')