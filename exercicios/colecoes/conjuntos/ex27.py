"""
Dada uma lista de números, mostre quais aparecem repetidos (dica: use um conjunto auxiliar de "já vistos").
"""
numeros = [1, 2, 3, 4, 5, 6, 2, 2, 3, 4]
ja_vistos = set()
repetidos = set()

for n in numeros:
    if n in ja_vistos:
        repetidos.add(n)
    else:
        ja_vistos.add(n)
        
print(f'Repetidos: {repetidos}')