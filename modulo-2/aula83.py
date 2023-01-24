#Empacotamento e desempacotamento de dicionários
# a, b = 1, 2
# a, b = b, a
# print(a, b)



# (a1, a2), (b1, b2) = pessoa.items()
# print (a1, a2)
# print(b1, b2)

# #for valor in pessoa.items():  #pega uma tupla no valor, empacota
# for chave, valor in pessoa.items(): #desempacota
#     print(valor)

#     #empacotar - por coisas no dictr
#     #desempacotar- tirar coisas no dictr


pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade' : 16,
    'altura': 1.6,
}
pessoa_completa = {**pessoa, **dados_pessoa}
# pessoas_completas = {**pessoa, 'chave':1}#acrescenta chave nova
# pessoas_completas = {**pessoa, 'nome':1}#muda o nome de índice 1
# pessoas_completas = {**pessoa, **dados_pessoa}
# print(pessoas_completas)

"""
args e kwargs
kwargs - keyword argumentos (argumentos nomeados) se usa 2 **

"""

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NAO NOMEADOS:', args)
    for chave, valor in kwargs.items():
        print(chave, valor)

# mostro_argumentos_nomeados(1,2, nome='Joana', qlq=123)
mostro_argumentos_nomeados(**pessoa_completa) #desempacotar

