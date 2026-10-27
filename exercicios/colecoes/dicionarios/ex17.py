"""
Agrupe uma lista de palavras pelo tamanho: {3: ['sol', 'mar'], 4: ['casa']}.
"""
texto = input('Digite um texto: ').lower().split()

dicionario = {}

for palavra in texto:
    if len(palavra) in dicionario:
        dicionario[len(palavra)].append(palavra)
    else:
        dicionario[len(palavra)] = [palavra]

print(dicionario)