"""
Leia números até o usuário digitar 0 (flag/sentinela) e mostre quantos foram digitados.
"""
num_digitados = 0

while True:
    num = input('Digite um número ou 0 p/ sair: ')

    try:
        num = int(num)
    except:
        print('Digite um número válido')
        raise

    if num == 0:
        break

    num_digitados += 1

print(f'Foram digitados {num_digitados} números')