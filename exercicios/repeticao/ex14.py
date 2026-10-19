"""
Mostre todos os primos de 1 a 100.
"""
for i in range(1, 101):
    qtd_divisores = 0

    for j in range(1, i + 1):
        if i % j == 0:
            qtd_divisores += 1
    
    if qtd_divisores == 2:
        print(i, end= ' ')