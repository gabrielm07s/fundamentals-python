"""
Dicionário de dicionários: {'alice': {'idade': 20, 'cidade': 'SP'}}; liste, adicione e altere dados de um usuário.
"""
dicionario = {'alice': {'idade': 20, 'cidade': 'SP'}}

for d in dicionario.items():
    print(d)

dicionario['alice']['pais'] = 'Araxá'
print(dicionario)

dicionario['alice']['pais'] = 'Holanda'
print(dicionario)