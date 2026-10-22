"""
Leia 10 números e mostre separadamente os pares e os ímpares (duas listas).
"""
numeros_pares = []
numeros_impares = []

for i in range(10):
    num = input('Digite um número: ')

    try:
        num = int(num)
    except:
        print('Digite um número válido')
        raise

    if num % 2 == 0:
        numeros_pares.append(num)
    else:
        numeros_impares.append(num)

print()
print(f'Números pares: {numeros_pares}')
print(f'Números ímpares: {numeros_impares}')

