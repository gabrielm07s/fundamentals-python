"""
Crie estatisticas(numeros) que devolve (menor, maior, media). 
Desempacote o resultado em três variáveis e mostre.
"""
def estatisticas(*numeros):
    return min(numeros), max(numeros), sum(numeros)/ len(numeros)

lista_numeros = [1, 2, 3, 4, 5, 6]
menor, maior, media = estatisticas(*lista_numeros)

print(f'Lista: {lista_numeros}')
print(f'Menor número da lista: {menor}')
print(f'Maior número da lista: {maior}')
print(f'Média dos números na lista: {media}')