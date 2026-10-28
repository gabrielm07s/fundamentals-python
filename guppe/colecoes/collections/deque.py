"""
Módulo Collections - Deque
Podemos dizer que deque é uma lista de alta performance
"""
from collections import deque

deq = deque('geek')
print(deq)

# Adicionando elementos no deque
deq.append('y') # adiciona ao final
print(deq)

deq.appendleft('k') # adiciona no começo da lista
print(deq)

# Remover elementos no deque
print(deq.pop()) # remove e retorna o último elemento
print(deq)

print(deq.popleft()) # remove e retorna o primeiro elemento
print(deq)