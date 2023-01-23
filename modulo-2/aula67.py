#Exercício com funções
"""

Crie uma função que multiplica todos os argumentos não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável

Crie uma função que fala se um número é par ou ímpar.
Retorne se o número é par ou impar
"""
x, y, *numeros = 1, 2, 3, 4, 5, 6, 7

def multiplicacao(*args):
    total = 1
    for numero in args:
        total*=numero
    print(total)
    return total

def impar_ou_par(numero):
    if numero % 2 ==0:
        print(f'O numero {numero} é par')
    else:
         print(f'O numero {numero} é ímpar')

#if multiplo_de_dois:
'''
    return f'{numero} é par'
    else:                           #esse else fica redundante pq ele vai direto pro return
        return f'{numero} é impar' 
'''

mult = multiplicacao(1, 2, 3, 4, 5)
verif = impar_ou_par(mult)
