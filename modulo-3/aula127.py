#Atributo de classe



class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual= 100
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

    
p1 = Pessoa ('Carolina', 19)
p2 = Pessoa ('Helena', 10)
# Pessoa.ano_atual = 1

print(Pessoa.ano_atual)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())