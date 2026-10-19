"""
Some os dígitos de um número inteiro (ex.: 1234 → 10) usando % e //.
"""
num = input('Digite um número: ')

try:
    num = int(num)
except:
    print('Digite um número válido')
    raise

num = abs(num)

soma_digitos = 0
valores = num

while True:
    soma_digitos += valores % 10
    valores //= 10

    if valores == 0:
        break

print(f'A soma dos valores do número {num} é: {soma_digitos}')