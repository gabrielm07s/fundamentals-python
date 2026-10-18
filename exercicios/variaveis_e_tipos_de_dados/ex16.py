"""
Leia um CPF no formato 12345678900 e imprima 123.456.789-00 usando fatiamento.
"""
cpf = input('Digite CPF: ')

cpf_formatado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

print(f'CPF original: {cpf}')
print(f'CPF formatado: {cpf_formatado}')