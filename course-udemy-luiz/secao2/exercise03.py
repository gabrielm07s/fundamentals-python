"""
Crie uma função que multiplica todos os argumentos não
nomeados recebido
Retorne o total para uma variável e mostre o valor da variável

Crie uma função que fale se um número é par ou ímpar
Retornar se é par ou ímpar
"""
def multiplica(*args):
    total = 1
    for num in args:
        total *= num
    
    return total

total = multiplica(1, 2, 3, 4, 5, 6)
print(f'O total é: {total}')

def par_ou_impar(n):
    return f'{n} é Par' if n % 2 == 0 else f'{n} é Ímpar'

print(par_ou_impar(2))
print(par_ou_impar(3))