"""
Higher Order Functions
Funções de primeira classe
"""
#voce pode jogar a função em uma variavel, passar como parâmetro para outras funções, retornar de dentro de outras funções

def saudacao(msg):
    return '{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

# v = saudacao_2('Bom dia')
# print(v)

v = executa(saudacao, 'Bom dia')
print(v)