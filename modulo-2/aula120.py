#Problema dos parâmetros mutáveis em funções python

def adiciona_clientes(nome, lista=None):# é recomendado n usar valores mutáveis
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

lista1 = []

cliente1 = adiciona_clientes('luiz', lista1)
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
cliente1.append('Edu')
print(cliente1)

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)
print(cliente2)