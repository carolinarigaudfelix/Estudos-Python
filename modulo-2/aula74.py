"""
 get - obtém uma chave
    pop - apaga um item com a chave especificada (del)
    popitem apaga o último item adicionado
    update - atualiza um dicionário com outro
"""

p1 = {
    'nome': 'Luiz',
    'sobrenome':'Miranda',
}

# print(p1['nome'])
# print(p1.get('nome', 'None'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# ultima_chave = p1.popitem()  #remove a ultima chave do dicionario
# print(ultima_chave)
# print(p1)

# p1.update({ #da pra atualizar as chaves existentes ou criar novas chaves e sem alterar as outras
#     'nome': 'novo valor'
# })
# print(p1)

# p1.update(nome='novo valor', idade=30)
# print(p1)
lista = ('nome', 'novo valor'),('idade',30)
tupla = (['nome', 'novo valor']),(['idade',30])
p1.update(lista)
print(p1)