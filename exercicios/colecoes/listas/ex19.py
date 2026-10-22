"""
Rotacione uma lista n posições para a direita ([1,2,3,4] com n=1 → [4,1,2,3]).
"""
lista = [1, 2, 3, 4]

n = input('Digte n posições para deslocar: ')

try:
    n = int(n)
except:
    print('Digite um número válido')
    raise

for i in range(n):
    ultimo_valor = lista[-1]
    for i in range(len(lista) - 1, -1, -1):
        if i == 0:
            lista[0] = ultimo_valor
        else:
            lista[i] = lista[i - 1]

print(lista)