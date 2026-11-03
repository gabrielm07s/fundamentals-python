"""
Crie eh_primo(n) e primos_ate(n), que devolve uma lista com os primos de 2 até n.
"""
def eh_primo(n):
    divisores = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisores += 1

    return True if divisores == 2 else False

def primos_ate(n):
    lista_primos = []
    for i in range(2, n + 1):
        if eh_primo(i):
            lista_primos.append(i)
    
    return lista_primos

n = int(input('Digite um número: '))
print(f'O número {n} é primo? {eh_primo(n)}')
print(f'Lista dos números primos de 2 até {n}: {primos_ate(n)}')