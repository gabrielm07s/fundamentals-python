"""
Try / Except / Else / Finally

Toda entrada do usuário deve ser tratada
Toda entrada deve ser tratada

else -> só entra se não acontecer o except (erro)
finally -> sempre é executado, independente se houve exceção ou não, geralmente usado para fechar ou desalocar
recursos
"""
num = 0

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')
finally:
    print('Executando o finally')

# Tratamento de erro completo
def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar divisão por zero'

num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')

print(dividir(num1, num2))