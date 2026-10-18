"""
Leia uma frase e mostre: tamanho, tudo maiúsculo, tudo minúsculo, primeira e última letra.
"""
frase = input('Digite uma frase: ')

print(f'Tamanho da frase: {len(frase)}')
print(f'Frase toda maiúscula: {frase.upper()}')
print(f'Frase toda minúscula: {frase.lower()}')
print(f'Primeira letra da frase: {frase[0]}')
print(f'última letra da frase: {frase[-1]}')