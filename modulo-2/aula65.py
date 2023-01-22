"""
Retorno de valores das funções (return)
"""

def soma(x, y):
    if x > 10:
        return 10
    return x + y


soma1 = soma(2, 3)
soma2 = soma(30, 3)

print(soma1 + soma2)

#print(variavel)  valor none
#variavel = print('Carolina')
#print(variavel is None) #verdadeiro
#isso ocorre porque função print é uma função pra saida do sistema, ela n armazena, print n tem valor

