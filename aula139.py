"""
Exercício com classes
1- Crie uma classe Carro (Nome)
2- Crie uma classe Motor (Nome)
3- Crie uma classe Fabricante (Nome)
4- Faça a ligação entre Carro tem Motor
Obs.: Um motor pode ser de vários carros
5- Faça a ligação entre Carro e Fabricante
Obs.: Um fabricante pode fabricar vários carros
Exiba o nome do carro, motor e fabricantes na tela
"""

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor    

    @property
    def fabricante(self):
        return self._fabricante    

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor    


class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

fusca = Carro('Fusca')
volkswagen = Fabricante('volkswagen')
motor_01 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_01
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)


# class Carro:
#     def __init__(self, nome):
#         self.nome = nome
#         self.fabricante = []
#         self.motor = []

#     def inserir_motor(self, nome):
#         self.motor.append(Motor(nome))

#     def inserir_fabricante(self, nome):
#         self.fabricante.append(Fabricante(nome))

#     def listar_motores(self):
#         for motores in self.motor:  
#             print(motores) 

#     def listar_fabricantes(self):
#         for fabricantes in self.fabricante:
#             print(fabricantes)         

# class Motor:
#     def __init__(self, nome):
#         self.nome = nome

# class Fabricante:
#     def __init__(self, nome):
#         self.nome = nome    

# carro1 = Carro('Fusca')
# carro1.inserir_motor('AWRSAD')
# carro1.inserir_fabricante('Toyota')   

# print(carro1.nome)
# carro1.listar_motores()
# carro1.listar_fabricantes()
