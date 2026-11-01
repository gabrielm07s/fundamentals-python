"""
Funções com Parâmetros (de entrada)

Funções que recebem dados para serem processados dentro da mesma

Um programa qualquer, temos:
    - Entrada -> Processamento -> Saída

Funções podem ter n parâmetros de entrada, ou seja, podemos receber como entrada em uma função
quantos parâmetros forem necessários, eles são separados por vírgulas
"""
def quadrado(num):
    return num ** 2

num = int(input('Digite um número: '))
print(f'O quadrado do número {num} é: {quadrado(num)}')

def soma(a, b):
    return a + b

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
print(f'A soma entre {a} e {b} é: {soma(a, b)}')

# Se informarmos um número errado de parâmetros ou argumentos, teremos TypeError
# Nomeando parâmetros

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo("Angelina", "Jolie"))

""" 
Diferença entre Parâmetros e Argumentos
Parâmetros são variáveis declaradas na definição de uma função
Argumentos são dados passados durante a execução de uma função

A ordem dos parâmetros importa
"""
nome = 'Felicity'
sobrenome = 'Jones'
print(nome_completo(sobrenome, nome))

# Argumentos nomeados (Keywords Arguments)
# Se usarmos os nomes dos parâmetros nos argumentos, podemos utilizar em qualquer ordem
print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(sobrenome=sobrenome, nome=nome))

## Erro comum na utilização do return
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total

lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))