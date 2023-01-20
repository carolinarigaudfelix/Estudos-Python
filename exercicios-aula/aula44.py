"""
Listas em Python
Tipo list - Mutável
Suporta várrios valores de qualquer tipo
Conhecimentos reutilizáveis - indíces e fatiamento
Métodos úteis : append, insert, pop, del, clear extend, +
criar, ler alterar, apagar = lista[i] (CRUD)-> create, read, update, delete

"""

# string = 'ABCDE' #5 caracteres(len)

# lista = [123,True,'Carol',1.2] #suporta vários valores de qualquer tipo

# print(lista, type(lista))
#evita ficar movendo muita coisa na lista, só retirar ou por no final

lista = [10, 20, 30 , 40]
lista[2] = 300
del lista[3]
print(lista)
print(lista[2])

lista.append(40) #adiciona ao final da lista
print(lista)
lista.pop() #remove ultimo item da lista
print(lista)