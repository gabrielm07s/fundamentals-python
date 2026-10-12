"""
Recebendo ados do usuário

input() => Todo dado recebido via input é do tipo string

Em Python, string é tudo o que estiver entre:
    - Aspas simples
    - Aspas duplas
    - Aspas simples triplas
    - Aspas duplas triplas
"""
# Entrada de Dados
nome = input("Qual é o seu nome? ")

# Exemplo de print antigo
# print("Seja bem-vindo(a) %s" % nome)

# Exemplo de print moderno
# print("Seja bem-vindo(a) {0}".format(nome))

# Exemplo de print atual
print(f'Seja bem-vindo(a) {nome}')

idade = int(input("Qual a sua idade? "))

# Exemplo de print atual
print(f'A {nome} tem {idade} anos')

# Exemplo de print moderno
# print("A {0} tem {1} anos".format(nome, idade))

# Exemplo de print antigo
# print("A %s tem %s anos" % (nome, idade))

"""
int(idade) => casting

Casting é a conversão de um tipo de dado em outro
"""
print(f'A {nome} nasceu em {2018 - idade}')