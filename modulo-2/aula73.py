"""
    Métodos úteis dos dicionários em Python
    len - quantas chaves
    keys - iterável com as chaves
    values - iterável com os valores
    items - iterável com chaves e valores
    setdefault - adiciona valor se a chave não existe
    copy - retorna uma cópia rasa (shallow copy)
    get - obtém uma chave
    pop - apaga um item com a chave especificada (del)
    popitem apaga o último item adicionado
    update - atualiza um dicionário com outro
"""
"""

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 900
}
pessoa.setdefault('idade', 0)
#print(pessoa.__len__()) #fala quantas chaves tem no dicionario
#print(list(pessoa.keys()))

#print(list(pessoa.value()))
print(list(pessoa.items()))
# for chave in pessoa:
#     print(chave)
# for valor in pessoa.values():
#     print(valor)
for chave, valor in pessoa.items():
    print(chave, valor)

"""
import copy

d1 = {
    'c1':1,
    'c2': 2,
    'l1': [0, 1, 2]
}

#d2 = d1.copy() #copia tudo que for imutável, se for mutável ele não copia e
# sim q os dois dicionarios apontem apra o msm lugar

d2 = copy.deepcopy(d1) #o deepcopy entra em todos os subniveis, tudo q é mutável

d2['l1'][1] = 9999999
 
d2['c1'] = 100
print(d1)
print(d2)