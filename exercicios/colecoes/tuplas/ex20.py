"""
Ordenação segura: dada uma tupla desordenada (45, 12, 89, 3, 27, 64), 
gere uma nova tupla com os elementos ordenados de forma crescente e outra de forma decrescente usando 
sorted() e tuple(). 
Confirme que a original não foi modificada.
"""
tupla = (45, 12, 89, 3, 27, 64)

tupla_crescente = tuple(sorted(tupla))
tupla_decrescente = tuple(sorted(tupla, reverse=True))

print(f'Tupla ordenada: {tupla_crescente}')
print(f'Tupla desordenada: {tupla_decrescente}')