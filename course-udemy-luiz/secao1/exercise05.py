num_str = input('Digite um número inteiro: ')

try:
    num_int = int(num_str)

    if num_int % 2 == 0:
        print(f'O número {num_int} é par')
    else:
        print(f'O número {num_int} é ímpar')
except:
    print('O numero não é inteiro')

# Outra forma poderia utilizar o métodos isdigit()