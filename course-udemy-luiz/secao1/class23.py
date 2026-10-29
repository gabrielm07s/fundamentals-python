"""
Formatação de Strings com f-strings
- s (string)
- d (int)
- f (float)
    .<n dígitos>f
- x / X (hexadecimal)

(caracterte)(><^)(quantidade)
- > (esquerda)
- < (direita)
- ^ (centro)

Sinal - + ou -
Ex: 0 >- 100,.1f

Conversion flags - !r !s !a
"""
variavel = 'ABC'

# PAD - espaçamento (preenchimento)
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}')

# float
print(f'{10000.4854564854785:+,.1f}')
print(f'{10000.4854564854785:-,.1f}')
print(f'{10000.4854564854785:0=+10,.1f}')

# conversion flag !r
print(f'{variavel!r}')
