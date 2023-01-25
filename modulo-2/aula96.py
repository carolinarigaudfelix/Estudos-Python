# raise - lançando exeções (erros) 
# se a função divide trata o erro é um problema, fica dificil nomear, é mt  coisa

# print(123)
# raise ValueError('Deu erro')
# print(456)

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir 0 que não é possivel')    
    return True

def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'{n} deve ser int ou float'
            f'{tipo_n.__name__} enviado.'
        )

def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)

    nao_aceito_zero(d)
    return n / d
    # try:
    #     return n/d
    # except ZeroDivisionError:
    #     print('_____')
    #     raise

print(divide(8,  0))