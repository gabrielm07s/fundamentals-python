"""
Crie dobro(n) que devolve o dobro de n. No programa principal, mostre dobro(7) e dobro(dobro(3)).
"""
def dobro(n):
    return n * 2

print(f'Dobro de 7: {dobro(7)}')
print(f'Dobro do dobro de 3: {dobro(dobro(3))}')