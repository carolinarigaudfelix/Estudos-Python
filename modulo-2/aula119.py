import json
#funções, métodos, classes, sets, não podem ser tacados em um jason

# pessoa = {
#     'nome': 'Carolina',
#     'sobrenome': 'Felix',
#     'enderecos' : [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55}
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }

# with open('aula119.json', 'w', encoding='utf8') as arquivo: #informa que tem json nesse arquivo
#     json.dump(
#         pessoa, 
#         arquivo, 
#         ensure_ascii=False, #o ensure usa os acentos certinho do sistema
#         indent= 2, #formata 
#         ) 


with open('aula119.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(type(pessoa))
#ele converte de um tipo pro outro
    print(pessoa['nome'])

#jason é uma estrutura simples de python