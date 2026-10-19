"""
Mostre o maior e o menor de uma sequência de 5 números lidos.
"""
for i in range(1, 6):
    num = input(f'Digite o {i}º número: ')

    try:
        num = int(num)
    except:
        print('Digite um número válido')
        raise

    if i == 1:
        maior = num
        menor = num
    
    if num > maior:
        maior = num
    
    if num < menor:
        menor = num

print()
print(f'MAIOR número da sequência: {maior}')
print(f'MENOR número da sequência: {menor}')
