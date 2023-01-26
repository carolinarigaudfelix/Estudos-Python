# from sys import path

# import aula100_package.modulo # nesse caso tem os namespaces são mt grandes #1
# # from aula100_package.modulo import soma_do_produto # é outra forma de importação, diminui o namespace #2
# from aula100_package import modulo #3 importa só o modulo
# from aula100_package.modulo import * #má prática

# print(aula100_package.modulo.soma_do_produto(1, 2))#1
# print(soma_do_produto(1, 2))#2
# print(modulo.soma_do_produto(1,2))#3
# print(soma_do_produto(2,3))
# print(variavel)
# #print(*path, sep='\n')  #path -> conjunto de strings que identificam um caminho ou diretório
# from aula100_package.modulo import fala_oi, soma_do_produto

# print(__name__)
# fala_oi()

from aula100_package import qualquer_coisa, soma_do_produto

print(soma_do_produto(2,3))
qualquer_coisa()

