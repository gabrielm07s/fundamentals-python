"""
Operadores Lógicos - and, or, not, is

# Operadores binários (dois operandos)
and (E LÓGICO)
or (OU LÓGICO)
is (É)

# Operadores unários (apenas um operando)
not (NEGAÇÃO)

AND - ambos as condições precisam ser True, se ao menos um for falso, a expressão resultará em falso
OR - se ao menos uma condição for True, a expressão resultará em true
NOT - inversão lógica da condição, se for True fica False e vice-versa
IS - estamos comparando um com o outro
"""
ativo = True
logado = False

if ativo and logado:
    print('Bem vindo(a) usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

if ativo or logado:
    print('Bem vindo(a) usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

if not ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem vindo usuário')

if ativo is False:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

