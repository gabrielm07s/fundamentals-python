"""
Módulo Collections - Default Dict 
- Não apresenta KeyError

Default Dict >> ao criar um dicionário com Default Dict, informamos um valor default
podendo utilizar um lambda para isso, esse valor será utilizado sempre que não houver um valor definido

Caso tentemos acessar uma chave que não existe, essa chave será criada e o vlaor default será atribuído

# dicionario = {'curso': 'Programação em Python: Essencial'}
# print(dicionario)
# print(dicionario['curso'])
# print(dicionario['outro']) # KeyError (chave não existe)

OBS! Lambdas são funções sem nome que podem ou não receber parâmetros de entrada e retornar valores
"""
from collections import defaultdict

dicionario = defaultdict(lambda: 0)
dicionario['curso'] = 'Programação em Python: Essencial'
print(dicionario)
print(dicionario['outro']) # coloca o valor padrão 0

