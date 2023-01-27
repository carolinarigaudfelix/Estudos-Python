#Variáveis livres + nonlocal (locals, global)
# def fora(x):
#     a = x #variável livre porque não está no escopo dentro

#     def dentro():
#         print(locals()) #mostra as variáveis locais do escopo
#         #print(dentro.__code__.co_freevars) #mostra as variáveis livres
#         return a
#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())

#print(globals())

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar = ''): # tem q passar um valor padrão pra concatenar
        nonlocal valor_final #nem global nem local, ele busca no escopo acima esas variável
        valor_final += valor_a_concatenar#tem que informar pro python que essa variável n é daq
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
