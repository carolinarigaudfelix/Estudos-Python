#Exercícios
#copy, sorted gera uma nova lista, ou lista.sort
"""
Aumenta os preços dos produtos a seguir em 10%
Gere novos_produtos por deep copy (cópia profunda)
"""
import copy
from dados import produtos


novos_produtos = copy.deepcopy(produtos)
for dado in novos_produtos:
    print(round(dado['preco']*1.1, 2))

lista_nome_ordenada = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'], reverse=True

)
lista_preco_ordenada = sorted(
    copy.deepcopy(produtos),
    key=lambda k: k['preco'],  reverse=True
)

for dado in lista_nome_ordenada:
    print(dado,sep='')
print()

for dado in lista_preco_ordenada:
    print(dado, sep ='')

# novos_produtos = [
#     {**p, 'preco': round(p['preco']*1.1, 2)} #criamos um dicionario q pega o p todo q é uma cópia dos produtos e usamos o round
#                                             # passando dois parâmetros, o elemento e as casas decimais
#     for p in copy.deepcopy(produtos) #[X] Copiar produtos
# ]

# produtos_ordenados_nome = sorted(
#     copy.deepcopy(produtos),
#     key=lambda p: p['nome'],
#     reverse=True

# )
# produtos_ordenados_preco = sorted(
#     copy.deepcopy(produtos),
#     key=lambda p: p['preco'],
#     reverse=True
    
# )
# print(*produtos, sep ='\n')
# print()
# print(*produtos_ordenados_nome, sep ='\n')
# print()
# print(*produtos_ordenados_preco, sep ='\n')

"""    
# for nova_lista in produtos:
#     print(nova_lista)

Ordene os produtos por nome decrescente (do maior pro menor)
Gere produtos_ordenados_por_nome por deep copy

Ordene os produtos por preco crescente (do menor para maior)
Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
"""