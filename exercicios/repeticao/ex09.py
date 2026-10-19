"""
Calcule o fatorial de n com while e depois com for.
"""
num = input('Digite um número: ')

try:
    num = int(num)
except:
    print('Digite um número válido')
    raise

i = num
fatorial = 1

while i >= 1:
    fatorial *= i
    i -= 1

"""
# loop for
for i in range(num, 0, -1):
    fatorial *= i
"""

print(f'O fatorial de {num} é: {fatorial}') 