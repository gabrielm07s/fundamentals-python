"""
Crie fatorial(n) sem recursão (com laço). Teste fatorial(0), fatorial(1) e fatorial(10).
"""
def fatorial(n):
    fatorial = 1
    for i in range(n, 0, -1):
        fatorial *= i
    return fatorial

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é: {fatorial(n)}')