"""
Funções recursivas e recursidade
funções que podem se chamar de volta
úteis p/ dividir problemas grandes em parte menores
Toda função recursiva deve ter
Um problema que possa ser dividido em partes menores
Um caso recursivo que resolve o pequeno problema
Um caso base que para a recursão
fatorial n" = 5* 4* 3* 2* 1 = 120
"""


# def recursiva(inicio=0, fim=4): #Caso recursivo, contar até chegar ao final
#     if inicio >=fim:
#         return fim

#     print(inicio, fim)

#     inicio +=1
#     return recursiva(inicio, fim)

# print(recursiva())
def fatorial(n):
    if n <=1:
        return 1

    return n * fatorial(n - 1)

print(fatorial(4)) 