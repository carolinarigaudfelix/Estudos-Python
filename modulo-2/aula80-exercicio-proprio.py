"""
Crie uma função que encontre o intruso menor de idade na festa.

Ex:[22,29,19,18,23,17]
Retorne: há um intruso na festa, ele tem 17 anos.
"""

lista_de_convidados = [
    [22, 29, 19, 18, 23, 17, 26, 29,17,15, 10]
]

def verifica_lista(lista_de_inteiros):
    lista_festa = set()
    menor_de_idade = 0

    for idade in lista_de_inteiros:
        if idade < 18:
            lista_festa.add(idade)
            menor_de_idade +=1

       
    return print(f'Há {menor_de_idade} intruso(s) na festa, ele(s) tem entre {lista_festa} anos.')



for lista in lista_de_convidados:
       verifica_lista(lista)
