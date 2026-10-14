n1 = input('Digite o 1º valor: ')
n2 = input('Digite o 2º valor: ')
n3 = input('Digite o 3º valor: ')

try:
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
except:
    print('Algum número digitado foi inválido')
    raise # Lança erro e finaliza o programa

soma = (n1 ** 2) + (n2 ** 2) + (n3 ** 2)
print(f'A soma dos quadrados entre os números {n1}, {n2} e {n3} é: {soma}')