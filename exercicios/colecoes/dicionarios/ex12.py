"""
Conte quantas vezes cada letra aparece em uma frase (dicionário de frequência).
"""
frase = input('Digite uma frase: ').replace(" ", "").lower()

dicionario = {}

for letra in frase: 
    dicionario[letra] = dicionario.get(letra, 0) + 1

print(dicionario)