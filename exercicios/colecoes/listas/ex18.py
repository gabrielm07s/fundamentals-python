"""
Dada uma lista de notas, mostre quantas estão acima da média.
"""
nota = [1.0, 2.2, 3.3, 5.5, 7.8, 9]
media = sum(nota) / len(nota)
acima_media = 0

for i in nota:
    if i > media:
        acima_media += 1

print(f'Acima da média: {acima_media}')