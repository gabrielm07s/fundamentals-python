"""
Concatenação de tuplas: crie uma tupla com 3 números pares e outra com 3 números ímpares. 
Concatene-as formando uma terceira tupla. Imprima as duas originais e a resultante.
"""
numeros_pares = (2, 4, 6)
numeros_impares = (1, 3, 5)

numeros = numeros_pares + numeros_impares

print(f'Números pares: {numeros_pares}')
print(f'Números ímpares: {numeros_impares}')
print(f'Números concatenados: {numeros}')