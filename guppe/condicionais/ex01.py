n1 = input('Digite o 1º número: ')
n2 = input('Digite o 2º número: ')

try:
    n1 = int(n1)
    n2 = int(n2)
except:
    print('Digite um número válido')
    raise

if n1 > n2:
    print(f'O número {n1} é maior que {n2}')
elif n2 > n1:
    print(f'O número {n2} é maior que {n1}')
else:
    print('Os dois valores são iguais')