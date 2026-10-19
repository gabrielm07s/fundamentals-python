"""
Mostre a sequência de Collatz de um número n até chegar a 1.

Sequência de Collatz:
1. Se o número for par, divida-o por 2 (n / 2).
2. Se o número for ímpar, multiplique-o por 3 e some 1 (3n + 1).
3. Repita o processo com o novo número obtido
"""
num = input('Digite um número: ')

try:
    num = int(num)
except:
    print('Digite um número válido')
    raise

num_operacao = num

print(num_operacao)
while True:
    if num_operacao == 1 or num_operacao < 1:
        break
    
    if num_operacao % 2 == 0:
        num_operacao //= 2
    else:
        num_operacao = (num_operacao * 3) + 1

    print(num_operacao)