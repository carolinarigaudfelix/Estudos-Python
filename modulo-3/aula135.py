"""
Encapsulamento (modificadores de acesso: public, protected, private)
Python não tem modificadores de acesso
Mas podemos seguir as seguintes convenções

    (sem underline) = public
        pode ser usado em qualquer lugar
    (um underline) = protected
        não DEVE ser usado fora da classe
        ou suas subclasses
    (dois underlines) = private
    _NomeClasse__nome_attr_ou_method
    "name mangling" (desfiguração de nomes) em Python
    só DEVE ser usado na classe que foi declarado.
"""
from functools import partial



class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__exemplo = 'Isso é private'

    def metodo_publico(self):
        # self._metodo_protected()
        # print(self._protected)
        print(self.__exemplo)
        self.__metodo_private()
        return 'metodo_publico'

    
    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'

    def __metodo_private(self):
        print('_metodo_private')
        return '_metodo_private'

f = Foo()
# print(f.public)
# print(f._protected)
print(f.metodo_publico())
print(f._Foo__metodo_private()) 