"""
Listas em Python
Tipo list -> Tipo Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
string = 'ABCDE' # caracteres (len)

# lista = list()
# print(bool([])) # falsy
# print(lista, type(lista))

# Cada vírgula separa um item diferente, nesse caso abaixo temos 5 
# itens
lista = [123, True, 'Luiz Otávio', 1.2, []]
print(lista)

print(lista[0]) # 123
lista[2] = 'Maria'
print(lista[2]) # 'Luiz Otávio'