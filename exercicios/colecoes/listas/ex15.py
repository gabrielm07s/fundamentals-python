"""
Leia nomes até o usuário digitar fim; depois mostre os nomes em ordem alfabética e quantos foram.
"""
lista_nomes = []

while True:
    nomes = input('Digite nomes ou "fim" para sair: ')

    if nomes == 'fim':
        break

    lista_nomes.append(nomes)

lista_nomes.sort()
print(f'\nQuantidade nomes: {len(lista_nomes)}')

print('Nomes em ordem alfabética: ')
for i in lista_nomes:
    print(f'- {i}')