"""
Dadas duas listas de convidados (festa A e festa B), mostre quem foi nas duas, quem foi só em A, quem foi só em B e o total de pessoas distintas.
"""
lista_convidadosA = ['A', 'B', 'C', 'D']
lista_convidadosB = ['B', 'E', 'C', 'F']

conjunto_convidadosA = set(lista_convidadosA)
conjunto_convidadosB = set(lista_convidadosB)

print(f'Pessoas que foram em ambas as festas: {conjunto_convidadosA.intersection(conjunto_convidadosB)}')
print(f'Pessoas que foram apenas na festa A: {conjunto_convidadosA.difference(conjunto_convidadosB)}')
print(f'Pessoas que foram apenas na festa B: {conjunto_convidadosB.difference(conjunto_convidadosA)}')
print(f'Total de pessoas distintas: {len(conjunto_convidadosA.union(conjunto_convidadosB))}')