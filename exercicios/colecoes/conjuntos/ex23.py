"""
Verifique se duas palavras são formadas pelas mesmas letras (ex.: amor e roma) comparando os conjuntos de letras.
"""
palavra1 = input('Digite a palavra 1: ')
palavra2 = input('Digite a palavra 2: ')

conjunto_palavras1 = set(palavra1)
conjunto_palavras2 = set(palavra2)

if conjunto_palavras1 == conjunto_palavras2:
    print(f'A palavra {palavra1} e a palavra {palavra2} são formados pelas mesmas letras: {conjunto_palavras2}')
else:
    print(f'A palavra {palavra1} e a palavra {palavra2} NÃO são formados pelas mesmas letras')