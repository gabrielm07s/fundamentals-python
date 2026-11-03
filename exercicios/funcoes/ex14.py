"""
Crie classificar_imc(peso, altura) que devolve o texto da classificação 
(abaixo do peso, normal, sobrepeso, obesidade). O programa principal lê os dados e mostra o resultado.
"""
def classificar_imc(peso, altura):
    imc = peso / (altura ** 2)

    if imc <= 18.5:
        classificacao = 'Baixo Peso'
    elif imc > 18.5 and imc < 25:
        classificacao = 'Peso Normal'
    elif imc >= 25 and imc < 30:
        classificacao = 'Sobrepeso'
    elif imc >= 30 and imc < 35:
        classificacao = 'Obesidade Grau I'
    elif imc >= 35 and imc < 40:
        classificacao = 'Obesidade Grau II'
    elif imc >= 40:
        classificacao = 'Obesidade Grau III'

    return f'IMC {imc:.1f}\nClassificação: {classificacao}'

peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))
print(f'Resultado: {classificar_imc(peso, altura)}')