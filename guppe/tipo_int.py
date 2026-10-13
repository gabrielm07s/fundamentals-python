"""
Tipo Numérico - int

São os números naturais e seus opostos

Operadores Aritméticos
    + - adição
    - - subtração
    * - multiplicação
    ** - exponenciação
    / - divisão
    // - divisão inteira
    % - módulo (resto da divisão)

podemos combinar operadores aritméticos com o operador de atribuição (=)   
    +=
    -=
    *=
    **=
    /=
    //=
    %=
"""
# Exemplo de inteiros
print(42)
print(-42)
print(1)

# Exemplo com operações
print('\n')
print(1 + 1)
print(1 - 1)
print(1 * 10)
print(10 ** 2)
print(10 / 2)
print(10 // 3)
print(10 % 2)

# Exemplo com mesclagem
print('\n')
num = 10

num += 10
print(num)

num -= 10
print(num)

num *= 10
print(num)

num **= 1/2
print(num)

num /= 10
print(num)

num //= 2
print(num)

num %= 2
print(num)

# Separando casas
print('\n')
print(1_0_0)
print(1_000_000)

# Verificando tipo numérico
print('\n')
print(type(1))