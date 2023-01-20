"""
enumerate - enumar iteráveis (índices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


# lista_enumerada = enumerate(lista, start=19)

# print(next(lista_enumerada))

# for item in lista_enumerada:
#     print(item)

"""
for indice, nome in lista_enumerada: #seleciona indice e nome pra guardar os dados
   print(indice, nome)
"""

for tupla_enumerada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumerada:
        print(valor)
