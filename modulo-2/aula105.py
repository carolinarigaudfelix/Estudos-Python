

# def multiplicacao(x):
#     def multiplicador(y):
#         return x*y
#     return multiplicador

# mult = multiplicacao(2)

# print(mult(3))


#
def criar_funcao(funcao):
    def interna(*args, **kwargs):
        for arg in args:
            is_string(arg)
        resultado = funcao(*args, **kwargs)
        return resultado
    return interna



def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Deve ser uma string.')


def inverte_string(string):
    return string[::-1]


reverse_check = criar_funcao(inverte_string)
reverse_string = inverte_string (123)
print(reverse_string)