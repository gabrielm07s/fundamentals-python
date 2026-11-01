def maior_valor(*args):
    return max(args)

lista_numeros = [4, 12, 12, 4, 3, 10, 20, 345]
print(f'Lista: {lista_numeros}')
print(f'O maior valor da lista é: {maior_valor(*lista_numeros)}')