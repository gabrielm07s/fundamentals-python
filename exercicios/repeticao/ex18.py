"""
Leia uma frase e conte vogais iterando letra por letra.
"""
frase = input('Digite uma frase: ').lower()

qtd_vogais = 0
vogais = ['a', 'e', 'i', 'o', 'u']

for letra in frase:
    if letra in vogais:
        qtd_vogais += 1

print(f'Quantidade totais de vogais: {qtd_vogais}')