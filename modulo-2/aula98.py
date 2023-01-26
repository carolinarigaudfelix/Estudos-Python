#Entendendo os seus próprios módulos Python
"""
O primeiro módulo executado chama-se _main_
você pode importar outro módulo inteiro ou parte do módulo
O python conhece a pasta onde o _main está e as pastas abaixo dele
Ele não reconhece pastas e módulos acim do _main_ por padrão
O python conhece todos os módulos e pacotes presentes nos caminhos de sys.path
O main é o ponto de partida do programa, ponto de entrada, dali em diante pode criar pacotes, módulos
"""
import aula98_m
from aula98_m import variavel_modulo, soma

# print('Este módulo se chama', __name__)
print(aula98_m.variavel_modulo)
print(variavel_modulo)
print(soma(2,3))
print(aula98_m.soma(2,3))