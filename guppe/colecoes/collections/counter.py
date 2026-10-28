"""
Módulo Collections - Counter (Contador)
Módulo Collections - High-performance Container Datetypes

Counter >> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é
parecido com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como
valor a quantidade de ocorrências desse elemento
"""
# Importando collections
from collections import Counter

# Podemos utilizar qualquer iterável, usando uma listsa
lista = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

res = Counter(lista)
print(res, type(res))

# Praticando e testando
texto = input('Digite um texto: ').lower()

letras = Counter(texto.replace(" ", ""))
palavras = Counter(texto.split())
print(letras)
print(palavras)

print(f'As 5 letras que apareceram mais vezes no texto digitado: {letras.most_common(5)}')
print(f'As 5 palavras que apareceram mais vezes no texto digitado: {palavras.most_common(5)}')