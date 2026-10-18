"""
Leia dois números com input() e mostre a soma como número (não concatenada). Explique por que '2' + '3' dá '23'.
"""
n1 = input('Digite o 1º número: ')
n2 = input('Digite o 2º número: ')

try:
    n1 = int(n1)
    n2 = int(n2)
except:
    print('Digite um número válido')
    raise

soma = n1 + n2

print(f'A soma entre {n1} e {n2} é: {soma}')

"""
'2' + '3' = '23'
Porque o operador de soma (+) com duas strings faz com que strings se concatenem (unem)
"""