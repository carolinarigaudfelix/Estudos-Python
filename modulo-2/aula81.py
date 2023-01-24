#
# Função lambda em Python
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo deve ser contido dentro de uma única expressão.
# 
lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome':'Carol', 'sobrenome': 'Felix'},
    {'nome':'Luisa', 'sobrenome': 'Santos'},
    {'nome':'Marcelo', 'sobrenome': 'Vieira'},
    {'nome':'Mônica', 'sobrenome': 'Pinheiro'},
]


# lista.sort(key=lambda item: item['sobrenome'])
def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key =lambda item: item['sobrenome'])

for item in lista:
    print(item)