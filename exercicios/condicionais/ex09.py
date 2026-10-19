"""
Leia um caractere e diga se é vogal ou consoante.
"""
caractere = input('Digite um caractere: ')

vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 
'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

if caractere.lower() in vogais:
    print('O caractere é uma VOGAL')
elif caractere.lower() in consoantes:
    print('O caractere é uma CONSOANTE')
else:
    print('Caractere não foi encontrado')