"""
Conte quantas vezes um valor lido aparece na lista 
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 1]

num = input('Digite um número: ')

try:
    num = int(num)
except:
    print('Digite um número válido')
    raise

qtd_valor = numeros.count(num)

# qtd_valor = 0
# 
# for numero in numeros:
#     if numero == num:
#         qtd_valor += 1

print(f'O número {num} apareceu {qtd_valor} vezes na lista: {numeros}')