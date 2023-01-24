#List comprehension em Python
#List comprehension é uma forma rápida para criar listas
#a partir de iteráveis

# print(list(range(10)))

lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

#lista = [numero for numero in range(10)] #inclui o numero em cada indice da lista, esse numero da esquerda define 
                               
lista  =[
    numero *2 #a esquerda do for põe uma lógica
    for numero in range(10)
]               
print(lista)