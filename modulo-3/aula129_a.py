"""
Exercício - Salve sua classe em JSON
Salve os dados da sua classe em JSON
e depois crie novamente as instâncias
da classe com os dados salvos
Faça em arquivos separados

"""
import json

CAMINHO_ARQUIVO = 'pessoas.json'

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

# dados = {'idade': 19, 'nome': 'Carolina'}
p1 = Pessoa ('João', 33)
p2 = Pessoa ('Helena', 21)
p3 = Pessoa ('Joana', 11)

grupo = [vars(p1), vars(p2), vars(p3)]

def fazer_dump():
    with open('pessoas.json', 'w', encoding='utf8') as arquivo:
                print('Fazendo Dump')
                json.dump(
                    grupo,
                    arquivo,
                    ensure_ascii=False,
                    indent=2
                )
                
if __name__ == '__main__':
    print('Ele é o __main__')
    fazer_dump()
"""
Resolução:
CAMINHO_ARQUIVO = 'aula127.json'

class Pessoa:
    class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade
    
    p1 = Pessoa ('João', 33)
    p2 = Pessoa ('Helena', 21)
    p3 = Pessoa ('Joana', 11)
    bd = [vars(p1, p2 , p3)]

    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, ident= 2)
"""            