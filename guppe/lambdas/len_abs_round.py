"""
Len, Abs, Sum, Round

len() - retorna o tamanho, o número de itens de um iterável

abs() - retorna o valor absoluto de um número inteiro ou real

sum() - recebe como parâmetro um iterável, podendo receber um valor inicial e retorna a soma total dos elemetnos, incluindo o valor inicial
OBS! O valor inicial default é 0

round() - retorna um número arredondado para n dígito de precisão após a casa decimal, se nao for informada retorna o inteiro mais próximo da entrada
"""
print('LEN:')
print(len('Geek University'))
print(len((1, 2, 3, 4, 5)))
print(len([1, 2, 3, 4, 5]))
print(len({1, 2, 3, 4, 5}))
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))
print(len(range(0, 10)))

# Por debaixo dos panos, quando usamos a função len(), o Python faz:
print('Geek University'.__len__) # Dunder len (__len__)

print('\nABS:')
print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))
# abs é somente com números

print('\nSUM:')
print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))
print(sum([3.145, 5.678]))
print(sum((1, 2, 3, 4, 5)))
print(sum({1, 2, 3, 4, 5}))
print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))

print('\nROUND:')
print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.21212121212121, 2))
print(round(1.2199999999, 2))
