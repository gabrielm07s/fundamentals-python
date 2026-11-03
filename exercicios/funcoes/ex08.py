"""
Crie estatisticas(numeros) que devolve (menor, maior, media). 
Desempacote o resultado em três variáveis e mostre.
"""
def estatisticas(*numeros):
    maior = max(numeros)
    menor = min(numeros)
    media = sum(numeros)/ len(numeros)
    print(f'Maior: {maior}')
    print(f'Menor: {menor}')
    print(f'Média: {media:.2f}')

lista_numeros = [1, 2, 3, 4, 5, 6]
estatisticas(*lista_numeros)