"""
Conte quantos números ímpares existem entre 1 e 500.
"""
qtd_impares = 0

for i in range(1, 501):
    if i % 2 != 0:
        qtd_impares += 1

print(f'A quantidade de números ímpares são: {qtd_impares}')