"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento) é convenção usar *args
"""

x, y, *resto = 1, 2, 3, 4 #empacota as variáveis em resto
print(x, y, resto)

# def soma(x, y):
#     return x + y

def soma(*args):#qualquer coisa q eu enviar ele empacota em tupla
    print(args, type(args)) #não pode alterar as tuplas
    total = 0 #acumulador
    for numero in args:
        total+=numero
    return (total)
soma_4_5_6= soma(4, 5, 6)
print(soma_4_5_6)

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9
outra_soma = soma(*numeros)

print(sum(numeros))