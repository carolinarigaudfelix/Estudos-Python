"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

nome = 'Luiz'
nome = 'João'
noutra_variavel = nome

print(nome)
print(noutra_variavel)

lista_a = ['Luiz', 'Maria']
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'

print(lista_a)
print(lista_b)


