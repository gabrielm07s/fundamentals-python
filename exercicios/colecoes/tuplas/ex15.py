"""
Desempacotamento estendido (*): crie uma tupla com 8 notas de avaliações. 
Usando o operador *, desempacote a primeira nota na variável primeira, a última na variável ultima e 
todas as do meio na lista intermediarias.
"""
avaliaçoes = (1.0, 2.5, 3.6, 5.7, 9.0, 10.5, 8.7, 6.8, 9.0, 9.0)

primeira_nota, *meio_notas, ultima_nota = avaliaçoes

print(f'Primeira nota: {primeira_nota}')
print(f'Notas do meio: {meio_notas}')
print(f'Última nota: {ultima_nota}')