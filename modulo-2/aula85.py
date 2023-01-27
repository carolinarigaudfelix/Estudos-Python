#Mapeamento de dados em list comprehension
import pprint #print bonito

produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30,},
]

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

novos_produtos = [
    # {'nome': produto['nome'], 'preco':produto['preco']} 
    {**produto, 'preco': produto['preco'] * 1.05} #aumenta cada preco pra 5%

    # produto['nome'] #preco 
    if produto['preco'] > 20 else {**produto} #ternário
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] *1.05)> 10

]

p(novos_produtos)

# lista = [n for n in range(10) if n <5] #o if da direita é um filtro, pra estabelecer uma condição

# print(lista)

# print(novos_produtos)
#print(*novos_produtos, sep='\n')


