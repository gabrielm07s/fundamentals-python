"""
Operadores Lógico (IN / NOT IN)

Strings são iteráveis, onde iterável quer dizer que é possível
navegar item a item
"""
nome = input("Qual o seu nome? ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
