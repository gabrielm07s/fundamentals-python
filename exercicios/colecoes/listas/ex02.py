"""
Adicione uma fruta no final, outra na posição 2 e remova uma. Imprima a lista após cada passo.
"""
frutas = ['Maçã', 'Banana', 'Laranja', 'Melão', 'Mexerica']

frutas.append('Melância')
print(frutas) # adicionada ao final da lista

frutas.insert(2, 'Kiwi') # adicionada no segundo local
print(frutas)

frutas.remove('Melão') # removendo a fruta 'Melão'
print(frutas)

print()
for fruta in frutas:
    print(fruta, end= ' ')