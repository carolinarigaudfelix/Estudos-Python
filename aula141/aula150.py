#Funções decoradoras e decoradores com classes
#Composição é melhor que herança

def adiciona_repr(cls): #criou uma função q recebe uma classe
    def meu_repr(self): #recebe self como se ela tivesse dentro da classe
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ =  meu_repr #atrela a função dentro da classe
    return cls

class MyReprMixin:
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr

@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

def meu_planeta(metodo):
        def interno(self, *args, **kwargs):
            resultado = metodo(self, *args, **kwargs) #evita recursividade, "sobreescreve" o metodo
            if 'Terra' in resultado:
                return 'Você está em casa'
            return resultado
        return interno

@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta
    def falar_nome(self):
        return f'O planeta é {self.nome}'

# Time = adiciona_repr(Time)
# Planeta = adiciona_repr(Planeta) Tem outra forma, pode por o decorador @adiciona_repr

brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)
print(terra)
print(marte)
print(terra.falar_nome())
print(marte.falar_nome())