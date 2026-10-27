"""
Mostre quem estuda só Python e quem estuda só Java, com difference() e depois com -.
"""
estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

somente_python = estudantes_python - estudantes_java
somente_java = estudantes_java - estudantes_python 

print(f'Somente Python: {somente_python}')
print(f'Somente Java: {somente_java}')