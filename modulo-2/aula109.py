"""
Considerando duas lsitas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho
da menor.


Exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_soma = [2, 4, 6, 8]
"""

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4, 8]
# lista_soma = [x + y for x, y in zip(lista_a, lista_b)]  MELHOR FORMA
# print(lista_soma)

def soma_lista (lista1, lista2):
    intervalo = min(len(lista1), len(lista2))
    return [(lista_a[i] + lista_b[i]) for i in range(intervalo)]


itens = soma_lista(lista_a, lista_b)
print(itens)

# lista_soma = []
# for i, _ in enumerate(lista_b):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)