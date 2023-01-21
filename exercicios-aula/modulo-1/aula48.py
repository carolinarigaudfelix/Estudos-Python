"""
Exercicio
Exiba os índices da lista
0 maria
1 helena 
2 luiz
"""



lista = ['Maria', 'Helena', 'Luiz']
teste = range(len(lista))
i=0
for nome in lista:
    nome = lista[i]
    print(f'{i} {nome}')
    i+=1

print(teste)

"""
lista = ['Maria', 'Helena', 'Luiz']
indices = range(len(lista))

for indice in indices:
    print(lista[indice], type(lista[indice]))
"""