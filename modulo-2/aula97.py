#Módulos padrão do Python(import, from, as e *)

# inteiro import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
# import sys

from sys import exit, platform

# print(platform)

#tomar cuidado pra não sobreescrever os nomes dos módulos quando importados desta forma


# import sys as s # muda o nome do módulo, mas n é o ideal
# # o python sobreescreve o módulo se você criar uma variável com o msm nome do módulo
# sys = 'alguma coisa'
# print(s.platform)
# print(sys)

# from sys import platform as pf
# from sys import exit as ex

# print(pf)



# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo

# alias 1 - import nome_modulo as apelido
# alias 2 - from nome_modulo import objeto as apelido
# vantegens: você pode reservar nomes para seu código
# desvantegens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# vantagens: importa tudo de um módulo
# desvantagens: importa tudo de um módulo

from sys import *# má prática
#from sys import exit, platform #boa prática
print(platform)
exit()
