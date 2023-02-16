# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import asdict, astuple, dataclass
#syntax sugar pra criar uma classe mais facil

@dataclass(repr=True, order=True) #congela a classe o frozen
class Pessoa:
    nome: str
    sobrenome: str

    # def __init__(self, nome, sobrenome):
    #     self.nome = nome
    #     self.sobrenome = sobrenome
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'

    # def __post_init__(self):
    #     print('POST INIT')

     # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'

    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)

if __name__ == '__main__':
    p1 = Pessoa('Luiz', 'Otávio')
    print(asdict(p1))
    print(astuple(p1))
    # lista = [ Pessoa('A', 'Z'), Pessoa('B', 'Z'), Pessoa('C', 'Z')]
    # ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome)
    # print(ordenadas)

    # p1 = Pessoa('Carol', 'Felix')
    # p1.nome = 'Maria'
    # p1.nome_completo = 'Maria Helena'
    # print(p1)
    # print(p1.nome_completo)