"""
Tipo list - Mutável
    append - adiciona ao final
    insert - adiciona um intem no indice escolhido
    pop- remove do final
    del- apaga um inidice
    clear - limpar a lista
    extend- estende a lista
"""

lista = [10,20,30,40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]
#lista.clear()

lista.insert(100,5)
print(lista[4])

