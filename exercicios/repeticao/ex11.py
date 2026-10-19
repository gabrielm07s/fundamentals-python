"""
Imprima os 10 primeiros termos da sequência de Fibonacci.
Fn = F(n-1) + F(n-2)
0, 1
"""
a = 0
b = 1
c = 0

for i in range(10): 
    if i == 0:
        print(a, end= ' ')
    elif i == 1:
        print(b, end= ' ')
    else:
        c = a + b
        a = b
        b = c
        print(c, end= ' ')