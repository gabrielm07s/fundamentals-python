"""
Dada a lista cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiabá', 'Campo Grande', 'São Paulo'], 
mostre quantas cidades existem na lista e quantas são distintas.
"""
cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiabá', 'Campo Grande', 'São Paulo']
print(f'Cidades existentes na lista: {len(cidades)}, sendo elas: {cidades}')

cidades_distintas = set(cidades)
print(f'Cidades distintas temos: {len(cidades_distintas)}, sendo elas: {cidades_distintas}')

