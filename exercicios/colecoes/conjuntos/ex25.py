"""
Sorteio de números sem repetição: use random.randint(1, 60) dentro de um while até o conjunto ter 6 números distintos. 
Mostre também quantos sorteios foram necessários.
"""
import random

conjunto_numeros = set()
sorteios = 0
while len(conjunto_numeros) < 6:
    numero_sorteado = random.randint(1, 60)
    sorteios += 1
    conjunto_numeros.add(numero_sorteado)

print(f'Conjunto de números: {conjunto_numeros}')
print(f'Quantidade de sorteios: {sorteios}')