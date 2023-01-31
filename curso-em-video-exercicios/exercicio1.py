"""
Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
"""


def tabuada(n,i=0):
    if i>10:
        return
    
    print(f'{n} * {i} =', n*i)

    i+=1
    return tabuada(n,i)


print(tabuada(2))