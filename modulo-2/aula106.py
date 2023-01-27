#Decoradores com parâmetros
# def fabrica_de_decoradores(a, b, c):
#     def fabrica_de_funcoes(func): #agr func recebe como parâmetro soma
#         print('Decoradora 1')

#         def aninhada(*args, **kwargs):
#             print('Aninhada')
#             res = func(*args, *kwargs)
#             return res
#         return aninhada
#     return fabrica_de_decoradores


# # def blablabla(a, b, c):
# #     return decoradora

# """
# quando você cria uma função e você mesmo executa essa função, o python espera uma função decoradora q recebe uma função
# então você pode ter acesso ao a, b e c
# """

# @fabrica_de_decoradores(1, 2, 3)
# def soma(x, y): #quando você executa uma função antes do python, ele tenta retornar, mas vc n chamou ela
#     return x + y


# decoradora = fabrica_de_decoradores
# multiplica = fabrica_de_decoradores(1, 2, 3)(lambda x, y: x * y)
# dez_vezes_cinco = multiplica(10, 5)

# print(dez_vezes_cinco)
# dez_mais_cinco = soma(10, 5)
# print(dez_mais_cinco)    

def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes



@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y

decoradora = fabrica_de_decoradores()
multiplica = decoradora(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)