"""
Exercício - Unir listas
Crie uma função zipper (como zipper de roupas)
O trabalho dessa função será unir duas listas na ordem.
Use todos os valores da menor lista

Ex: ['Salvado', 'Ubatuba', 'Belo Horizonte']
    ['BA', 'SP', 'MG', 'RJ']

    Resultado:
    [('Salvador', 'BA'), ('Ubatuba', 'SP), ('Belo Horizonte', 'MG')]
"""
import copy

municipios = ['Salvador', 'Ubatuba', 'Belo Horizonte']
siglas =['BA', 'SP', 'MG', 'RJ']

#min(len(lista1), len(lista2))
from itertools import zip_longest
def ziper(list1, list2):

    interna = [(list1[i], list2[i]) for i in range (0, len(list1))]
    return interna


print(ziper(municipios, siglas))
#print(list(zip(l1, l2)))
#print(list(zip_longest(l1, l2))) #considera a lista maior

"""
def zipper(lista1, lista2):
    intervalor_maximo = min(len(lista1), len(lista2)) serve pra pegar o máximo da lista da função
    return[
        (lista[i] for i in range(intervalo_maximo))
    ]

    print(zipper(l1, l2))
"""
