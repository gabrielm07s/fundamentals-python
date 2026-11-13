"""
Bloco try/except

O bloco try/except é usado para tratar erros qeu podem ocorrer em nosso código, prevenindo
que o programa para de funcionar e que o usuário receba mensagens de erro inesperadas

Sintaxe:

try:
    // execução problemática
except:
    // o que deve ser feito em caso de problema

OBS! Tratar erro de forma genérica não é a melhor forma de tratamento de erros, o ideal é tratar de forma específica
"""
# Tratando um erro genérico
try:
    geek()
except:
    print('Trantando o erro')

# Tratando erro específicos
try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# Com diferentes tipos de erros
try:
    len(5)
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')

# Tratando erros em funções
def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None

dic = {'nome': 'Geek'}
print(pega_valor(dic, 'Nome'))