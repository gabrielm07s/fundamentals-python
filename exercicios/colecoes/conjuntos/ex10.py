"""
Leia 5 nomes do teclado, guarde-os em um conjunto e mostre quantos nomes distintos foram digitados.
"""
conjunto_nomes = set()

for i in range(5):
    nome = input(f'Nome [{i + 1}]: ')
    conjunto_nomes.add(nome)

print(conjunto_nomes)
print(f'Quantidade de nomes distintos registrados: {len(conjunto_nomes)}')

