"""
class - Classes são moldes para criar novos objetos
As classes geram novos objetos (instâncias) que
podem ter seus próprios atributos e métodos.
Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações.
Por conveção, usamos PascalCase para nomes de classes
Pascal case - toda palavra com letra maiúscula ex: CriaBaseDeDados
"""
#string= 'Luiz' #str
#print(string,upper()
#print(isinstance(string,str)))

class Pessoa:
    ...

p1 = Pessoa()
p1.nome = 'Luiz'
p1.sobrenome = 'Otávio'
print(p1.nome)
print(p1.sobrenome)

p2 = Pessoa()
p2.nome = 'Luiza'
p2.sobrenome = 'Miranda'
print(p2.nome)
print(p2.sobrenome)