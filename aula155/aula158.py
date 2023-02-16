# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass, field #configura os campos na data class
#syntax sugar pra criar uma classe mais facil

@dataclass(repr=True, order=True) #congela a classe o frozen
class Pessoa:
    nome: str = field(
        default='MISSING', repr=False
    )
    sobrenome: str = 'Not sent'
    idade: int = 100
    enderecos: list[str] = field(default_factory=list) #sempre q n existir um 
    #endereço, chama essa função list e cria um endereco

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
    p1 = Pessoa()
    #print(fields(p1)) RETORNA A CONFIGURAÇÃO DOS CAMPOS
    print(p1)

    # lista = [ Pessoa('A', 'Z'), Pessoa('B', 'Z'), Pessoa('C', 'Z')]
    # ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome)
    # print(ordenadas)

    # p1 = Pessoa('Carol', 'Felix')
    # p1.nome = 'Maria'
    # p1.nome_completo = 'Maria Helena'
    # print(p1)
    # print(p1.nome_completo)