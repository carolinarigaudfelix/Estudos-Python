"""
Dicionários em Python (tipo dict)

Dicionários são estruturas de dados do tipo
par de "chave" e "valor"

Chaves pode ser consideradas como o "índice"
que vimos na lsita e podem ser de tipos imutáveis
como:str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro dicionário
Usamos as chaves {} ou a classe dict para criar dicionários
Imutáveis: str, int, float, bool, tuple
Mutáveis: dict, list
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura: 1.8,
    'endereços': [
        {'rua': 'tal tal ', 'número': 123}
        {'rua': 'outra}
    ]
}
print(pessoa, type(pessoa))
"""
#pessoa = dict(nome='Carolina', sobrenome='Felix')
pessoa = {
    'nome': 'Carolina',
    'sobrenome': 'Felix',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra', 'número': 321},
    ]
}

print(pessoa['nome'])
print(pessoa['sobrenome'])

for chave in pessoa:
    print(chave, pessoa[chave])