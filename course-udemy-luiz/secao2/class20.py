# Empactoamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}
(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)

def mostro_args(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_args(nome='Joana', qlq=123)
mostro_args(**pessoa_completa)