"""
Conversão / Coerção de tipos
Outros nomes: Type Casting, Type Conversion, Type Coercion

É o ato de converter um tipo em outro tipo

Tipos imutáveis e primitivos:
    str, int, float, bool
"""
#print('1' + 1) # TypeError: can only concatenate str (not "int") to str
print('a' + 'b') # Concatenção de strings
#print('a' + 1) # TypeError: can only concatenate str (not "int") to str

# Convertendo string -> int
print(type(int('1')))

# Convertendo string -> float
print(type(float('1.1')))

# Convertendo int -> string
print(type(str(1)))

# Convertendo float -> string
print(type(str(1.1)))

# Convertendo para booleano
print(type(bool(1))) # True
print(type(bool(0))) # False