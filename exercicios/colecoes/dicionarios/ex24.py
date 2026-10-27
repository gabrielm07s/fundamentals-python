"""
Conversor de números romanos simples (I, V, X, L, C, D, M) usando um dicionário.
"""
numeros_romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

numero = input('Digite um número romano: ').upper()

total = 0
for num in range(len(numero) - 1):
    valor_atual = numeros_romanos[numero[num]]
    proximo_valor = numeros_romanos[numero[num + 1]]

    if valor_atual >= proximo_valor:
        total += valor_atual
    else:
        total -= valor_atual

total += numeros_romanos[numero[-1]]        

print(f'Número: {total}')