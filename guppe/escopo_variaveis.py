"""
Escopo de variáveis

Dois casos de escopo em Python:

1 - Variáveis globais: são reconhecidas, ou seja, seu escopo compreende, todo o programa

2 - Variáveis locais: são reconhecidas, ou seja, seu escopo compreende, apenas no bloco onde foram declaradas, ou seja,
seu escopo está limitado ao bloco onde foi declarada

Declarar variáveis em Python:

nome_variavel = valor_variavel

Python é uma linguagem de tipagem dinâmica, ou sjea, não precisamos colocar o tipo de dfado a ela, este tipo é inferido
ao atribuírmos o valor a mesma
"""
numero = 42 # variável global 
print(numero, type(numero))

if numero > 10:
    novo = numero + 10 # variável loval, declarada localmente dentro do bloco if
    print(novo)

print(novo)