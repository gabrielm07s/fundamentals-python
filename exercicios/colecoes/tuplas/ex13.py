"""
Tuplas a partir de texto: leia uma frase do teclado e gere duas tuplas: 
    - uma formada por cada caractere da frase (tuple(frase)) e 
    - outra formada pelas palavras separadas (tuple(frase.split())). Imprima ambas.
"""
texto = input('Digite um texto: ')

tupla_caractere = tuple(texto)
tupla_palavras = tuple(texto.split())

print(f'Tupla caractere: {tupla_caractere}')
print(f'Tupla palavras: {tupla_palavras}')