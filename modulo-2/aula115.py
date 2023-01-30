#reduce - faz a redução de um iterável em um valor
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.00},
    {'nome': 'Produto 3', 'preco': 2.00},
    {'nome': 'Produto 2', 'preco': 6.00},
    {'nome': 'Produto 4', 'preco': 4.00},
]
 #reduce precis de um acumulador também

def funcao_do_reduce(acumulador, produto):
    print('acumulador', acumulador)
    print('produto', produto)
    print()
    return acumulador + produto['preco']

    
total = reduce(
    # funcao_do_reduce,
    lambda ac, p: ac + p['preco'],
    produtos,
    0 #valor inicial, qnd passa o valor inicial o primeiro produto equivale a ele em seu indice
)
print(f' o total é {total}')

#print(sum([p['preco'] for p in produtos]))
# for p in produtos:
#     total += p['preco']

# print(total)
