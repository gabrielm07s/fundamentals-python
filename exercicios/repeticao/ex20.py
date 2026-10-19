"""
Inverta um número inteiro usando só aritmética (1234 → 4321).
"""
num_original = input('Digite um número: ')

try:
    num_original = int(num_original)
except:
    print('Digite um número válido')
    raise

num_original = abs(num_original)

num_inverso = 0
valores = num_original

while True:
    num_inverso = (num_inverso * 10) + (valores % 10)

    valores //= 10
    
    if valores == 0:
        break

print(f'O número {num_original} ao contrário é: {num_inverso}')
