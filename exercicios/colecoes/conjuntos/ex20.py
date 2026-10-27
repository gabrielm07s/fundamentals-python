"""
Dados dois conjuntos de números lidos do teclado (5 em cada), mostre os números em comum, 
os que aparecem só no primeiro e os que aparecem só no segundo.
"""
print('Conjunto 1:')
conjunto1 = set()
for i in range(5):
    num = int(input(f'Digite o [{i + 1}º] número: '))
    conjunto1.add(num)

print('\nConjunto 2:')
conjunto2 = set()
for i in range(5):
    num = int(input(f'Digite o [{i + 1}º] número: '))
    conjunto2.add(num)

numeros_comum = conjunto1 & conjunto2
numeros_conjunto1 = conjunto1 - conjunto2
numeros_conjunto2 = conjunto2 - conjunto1

print(f'\nConjunto 1: {conjunto1}')
print(f'Conjunto 2: {conjunto2}')
print(f'Números em comum nos dois conjuntos: {numeros_comum}')
print(f'Números pertencentes apenas ao conjunto 1: {numeros_conjunto1}')
print(f'Números pertencentes apenas ao conjunto 2: {numeros_conjunto2}')