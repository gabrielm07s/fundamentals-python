"""
Contagem e busca: leia 5 números em uma tupla e informe:
Quantas vezes o número 9 apareceu (.count());
Em qual índice o primeiro valor 3 foi digitado (.index()), 
tratando com if ou try/except para não quebrar caso o 3 não tenha sido digitado.
"""
numeros = ()

for i in range(5):
    num = input(f'Digite o {i}º número: ')

    try:
        num = int(num)
    except:
        print('Digite um número válido')
        raise

    tupla_num_atual = (num, )
    numeros += tupla_num_atual

tres_existe = 3 in numeros

print('\nResultados:')
print(f'O número 9 apareceu {numeros.count(9)} vezes')

if tres_existe:
    print(f'O índice do primeiro 3 é: {numeros.index(3)}')
else:
    print('O número 3 não foi digitado')

