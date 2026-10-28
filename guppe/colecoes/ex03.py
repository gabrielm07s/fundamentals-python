numeros = []
for i in range(10):
    num = int(input(f'Digite o {i + 1}º número: '))
    numeros.append(num)

numeros_pares = 0

for n in numeros:
    if n % 2 == 0:
        numeros_pares += 1

print(f'NÚMEROS: {numeros}')
print(f'TOTAL DE NÚMEROS PARES: {numeros_pares}')