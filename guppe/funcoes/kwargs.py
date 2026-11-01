"""
**kwargs

É um parâmetro que diferente do *args que coloca valores extras em uma tupla, o **kwargs exige que utilizemos
parâmetros nomeados e transforma esses parâmetros extas em um dicionário

OBS! os parâmetros *args e os **kwargs não são obrigatórios
"""
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')
cores_favoritas()

# Desempacotar com **kwargs
def mostrar_nomes(**kwargs):
    return f'{kwargs['nome']} {kwargs['sobrenome']}'

nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}
print(mostrar_nomes(**nomes))

def soma(a, b, c):
    print(a + b + c)

dicionario = dict(a=1, b=2, c=3)
soma(**dicionario)

# OBS! Os nomes da chave em um dicionário devem ser o mesmo dos parâmetros da função