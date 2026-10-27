"""
Conte a frequência de cada palavra de um texto.
"""
texto = input('Digite um texto: ').lower().split()

dicionario = {}

for palavra in texto:
    dicionario[palavra] = dicionario.get(palavra, 0) + 1

print(dicionario)