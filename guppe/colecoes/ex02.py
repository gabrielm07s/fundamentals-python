A = []
for i in range(6):
    num = int(input(f'Digite o {i + 1}º número: '))
    A.append(num)

soma = A[0] + A[1] + A[5]
print(f'Soma dos itens {A[0]}, {A[1]} e {A[5]}, que resulta em: {soma}')
A[5] = 100

for i in A:
    print(i)