"""
Crie somar(a, b) e maior(a, b) (sem usar max), que devolvem o resultado. Teste com assert.
"""
def somar(a, b):
    return a + b

def maior(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return a

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print(f'A soma entre {n1} e {n2} é {somar(n1, n2)}')
print(f'O maior número entre {n1} e {n2} é: {maior(n1, n2)}')