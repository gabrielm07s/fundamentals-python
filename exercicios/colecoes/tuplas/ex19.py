"""
Mutabilidade interna: crie uma tupla t = (1, 2, ['A', 'B']). 
Adicione 'C' à lista interna usando append. 
Mostre a tupla resultante e explique 
por que a tupla permaneceu com os mesmos identificadores e sem quebrar a regra de imutabilidade.
"""
t = (1, 2, ['A', 'B'])

t[2].append('C')
print(t)