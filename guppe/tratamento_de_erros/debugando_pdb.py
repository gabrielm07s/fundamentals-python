"""
Debuggando com PDB

Sendo PDB -> Python Debugger
Bug -> inseto
"""
def dividir(a, b):
    try:
        # print(a, b)
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4, 7))
# A utilização da função print() é uma má prática de debugger
# Usando o debugger