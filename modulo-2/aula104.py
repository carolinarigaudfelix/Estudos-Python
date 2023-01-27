#Funções decoradoras e decoradores
"""
Decorar = Adicionar / Remover / Restringir / Alterar
Funções decoradoras são funções que decoram outras funções
Decoradores são usadas pra fazer o Python 
usar as funções decoradoras em outras funções
#Decoradores são "Syntax Sugar" (açúcar sintático)

"""
def criar_funcao(func):         #função decoradora, recebe uma função, cria uma função interna e ela não sera executada,
    def interna(*args, **kwargs):  #só retornada
        #print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        #print('Ok agora você foi decorado')
        return resultado
    return interna


"""
função dentro da função, 
"""

@criar_funcao #agora a inverte_string se torna a função interna
def inverte_string(string):
    print(f'{inverte_string.__name__}') 
    return string[::-1]

# def is_string(param):

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


inverte_string_checando_parametro = criar_funcao(inverte_string) #com base na nossa função, criamos outra usando ela de param

#invertida = inverte_string_checando_parametro('123') # se a string fosse um numero: ex:inverte_string'123' daria problema
invertida = inverte_string('123')
print(invertida)

