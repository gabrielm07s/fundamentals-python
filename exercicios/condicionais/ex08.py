"""
Leia um ano e diga se é bissexto (divisível por 4 e não por 100, ou divisível por 400).
"""
ano = input('Digite um ano: ')

try:
    ano = int(ano)
except:
    print('Digite um valor válido')
    raise

bissexto = (ano % 4 == 0) and ((ano % 100 != 0) or (ano % 400 == 0))

if bissexto:
    print(f'O ano {ano} É BISSEXTO')
else:
    print(f'O ano {ano} NÃO É BISSEXTO')
    