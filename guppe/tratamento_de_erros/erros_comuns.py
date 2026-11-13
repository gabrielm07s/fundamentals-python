"""
Erros mais comuns em Python

É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução do nosso código

Os erros mais comuns:

SyntaxError -> quando o Python encontra um erro de sintaxe, quando escreve algo que o Python não reconhece como parte
da linguagem

# Exemplos
a) 
def funcao:
    print('Geek University')

b)
None = 1

c)
return

NameError -> ocorre quando uma variável ou função não foi definida

# Exemplos
a)
print(geek)

b)
geek()

c)
a = 18
if a < 10:
    msg = 'é MENOR que 10'
print(msg)

TypeError -> ocorre quando uma função/operação é aplicada a um tipo errado

# Exemplos
a)
print(len(5))

b)
print('Geek' + [])

IndexError -> ocorre quando tentamos acesssar um elemento em uma lista ou outro tipo de dado indexado utilizando
um índice inválido

# Exemplos
a)
lista = ['Geek']
print(lista[2])

b)
lista = ['Geek']
print(lista[0][10])

ValueError -> quando uma função/operação built-in (integrada) recebe um argumento com um tipo correto porém com
valor inapropriado

# Exemplos
a)
print(int('Geek'))

KeyError -> ocorre quando tentamos acessar um dicionário com uma chave que não existe

# Exemplos
a) 
dic = {}
print(dic['geek'])

AttributeError -> ocorre quando uma variável não tem atributo ou função

# Exemplos
a)
tupla = (11, 2, 31, 4)
print(tupla.sort())

IdentationError -> ocorre quando não respeitamos a identação do Python (4 espaços)

# Exemplos
a)
def nova();
print('Geek')
"""

