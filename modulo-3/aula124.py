# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)
# Métodos em instâncias em classes Python
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar váris instâncias
# Na classe o self é a própria instância
# Hard coded - É algo que foi escrito diretamente no código

class Carro:
    def __init__(self, nome): ##digita def __ e aperta tab sempre retorna none
        self.nome = nome

    def acelerar(self): #sempre tem q por o self
        print(f'O carro {self.nome} está acelerando')


fusca = Carro('Fusca')
fusca.acelerar()
Carro.acelerar(fusca)
# Carro.acelerar() isso é chamar os moldes
# print(fusca.nome)
# fusca.acelerar()

celta = Carro(nome ='Celta')
celta.acelerar()
Carro.acelerar(celta)
# print(celta.nome)
# celta.acelerar()