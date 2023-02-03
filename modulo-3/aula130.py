"""
Métodos de classe
São métodos onde "self" será "cls", ou seja,
ao invés de receber a instância no primeiro
parâmetro, receberemos a própria classe.
"""

class Pessoa:
    ano = 2023 #atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod #chama classe sem passar self, passa a propria classe em si
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)


p1 = Pessoa('João', 24)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa('Anônima', 34)
p4 = Pessoa.criar_sem_nome(25)

print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)
# print(Pessoa.ano)
# Pessoa.metodo_de_classe()
