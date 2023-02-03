# __dict__ e vars para atributos de instância

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade



dados = {'idade': 25, 'nome': 'João'}
p1= Pessoa(**dados)
# p1.nome = 'Eita'
# del p1.nome
#print(p1.idade)
# p1.__dict__['outra'] = 'coisa'
# p1.__dict__['nome'] = 'Eita'
# del p1.__dict__['nome']
print(vars(p1)) #mostra o disct do objeto
print(p1.nome)
# print(p1.outra) #mostra os elementos do objeto
