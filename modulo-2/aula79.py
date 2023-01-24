"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo número com a duplicação.
Retorne a duplicação considerada.

Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
    [1, 2, 3, 4, 2, 1] -> 1, 2 e 3 são duplicados (Retorne 3)
    [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
    Se não encontrar duplicados, retorne -1

"""

lista_de_listas_de_inteiros = [

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],

]

def encontra_primeiro_duplicado(lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in lista_de_inteiros:
        if numero in numeros_checados:
           primeiro_duplicado = numero
           break
        
        numeros_checados.add(numero)

    print()
    print()
    return primeiro_duplicado

for lista in lista_de_listas_de_inteiros:
    print(
        lista,
        encontra_primeiro_duplicado(lista)
    )
    

    