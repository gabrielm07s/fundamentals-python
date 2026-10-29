"""
split e join com list e str

split - divide uma string
join - une uma string
"""
frase = 'Olha só que, coisa interessante'

lista_palavras = frase.split()
print(lista_palavras)

lista_frases = frase.split(', ')
print(lista_frases)

lista_frases = frase.split(',') # deixando um espaço proposital
for i, frase in enumerate(lista_frases):
    print(lista_frases[i].strip())

# rstrip() - remove espaçoes em branco no final da str
# lstrip() - rmove espaços em branco no inicio da str
# strip() - remove espaços em branco no inicio e fim da str

# unindo frases
frases_unidas = '-'.join('abc') # passamos um iterável
print(frases_unidas)