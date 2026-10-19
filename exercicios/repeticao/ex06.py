"""
Leia 10 números e mostre a soma e a média.
"""
soma = 0
media = 0

for i in range(1, 11):
    num = input(f'Digite o {i}º número: ')

    try:
        num = int(num)
    except:
        print('Digite um número válido')
        raise

    soma += num

media = soma / 10

print(f'A média dos números é de: {media:.2f}')