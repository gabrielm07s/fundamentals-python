"""
Leia 4 valores inteiros do teclado e armazene-os diretamente em uma tupla. Imprima a tupla lida, a soma (sum), 
o maior elemento (max) e o menor elemento (min).
"""
tupla_numeros = ()

for i in range(4):
    num = input(f'Digite o {i + 1}º número: ')

    try:
        num = int(num)
    except:
        print('Digite um número válido')
        raise

    tupla_num_atual = (num, )
    tupla_numeros += tupla_num_atual

print(f'\nTupla: {tupla_numeros}')
print(f'Soma tupla: {sum(tupla_numeros)}')
print(f'Maior elemento tupla: {max(tupla_numeros)}')
print(f'Menor elemento tupla: {min(tupla_numeros)}')
