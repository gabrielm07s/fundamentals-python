num = input('Digite um número inteiro: ')

try:
    num = int(num)
except:
    print('Número inválido')

print(f'O número digitado foi {num}')