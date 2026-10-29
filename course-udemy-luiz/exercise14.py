import random

nove_digitos_cpf = ''

for i in range(9):
    nove_digitos_cpf += str(random.randint(0, 9))

contador1 = 10
resultado1 = 0
for digito1 in nove_digitos_cpf:
    resultado1 += int(digito1) * contador1
    contador1 -= 1 

resultado1 = (resultado1 * 10) % 11
primeiro_digito = resultado1 if resultado1 <= 9 else 0
# print(f'Primeiro dígito é: {primeiro_digito}')

dez_digitos_cpf = nove_digitos_cpf + str(primeiro_digito)
contador2 = 11
resultado2 = 0
for digito2 in dez_digitos_cpf:
    resultado2 += int(digito2) * contador2
    contador2 -= 1

resultado2 = (resultado2 * 10) % 11
segundo_digito = resultado2 if resultado2 <= 9 else 0
# print(f'Segundo dígito é: {segundo_digito}')

cpf_gerado = nove_digitos_cpf + str(primeiro_digito) + str(segundo_digito)

print(cpf_gerado)