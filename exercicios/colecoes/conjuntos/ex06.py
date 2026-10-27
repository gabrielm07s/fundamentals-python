"""
Leia um número do teclado e diga se ele está em um conjunto {3, 6, 9, 12} (use in).
"""
conjunto = {3, 6, 9, 12}

num = int(input('Digite um número: '))

if num in conjunto:
    print(f'O número {num} está no conjunto')
else:
    print(f'O número {num} NÃO está no conjunto')