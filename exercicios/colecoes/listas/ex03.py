"""
Leia 5 números e guarde-os numa lista. Imprima a lista, a soma, a média, o maior e o menor.
"""
lista = []

for i in range(5):
    num = input('Digite um número: ')

    try:
        num = int(num)
    except:
        print('Digite um número válido')
        raise

    lista.append(num)

soma = sum(lista)
media = soma / len(lista)

print(f'\nLista: {lista}')
print(f'Soma de elementos: {soma}')
print(f'Média dos elementos: {media:.2f}')
print(f'Maior: {max(lista)}')
print(f'Menor: {min(lista)}')
