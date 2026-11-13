"""
Try, except, else e finally

finally sempre será executado
else é executado caso o bloco for executado sem erro
"""
try:
    print(111)
    8 / 0
except ZeroDivisionError:
    print('Divisão por zero')
else:
    print('Bloco else')
finally:
    print(222)