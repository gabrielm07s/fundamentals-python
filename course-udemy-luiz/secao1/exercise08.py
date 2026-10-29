"""
Iterando strings com while
"""
nome = 'Luiz Otávio' # iteráveis
novo_nome = ''
contador = 0

while contador < len(nome):
    novo_nome += nome[contador] + '*' 
    contador += 1

print(novo_nome)