#sys.argv - Executando arquivos com argumentos no sistema
#Fonte = Fira Code

import sys
argumentos = sys.argv
argumentos.append('batata1')
argumentos.append('batata2')
argumentos.append('batata3')
qtd_argumentos = len(argumentos)
#o primeiro argumento sempre é o módulo 

print(qtd_argumentos)
if qtd_argumentos <=1:
    print('Você só passou um argmumento')
else:
    try:
        print(f'Você passou os argumentos {argumentos[1:]}')
        print(f'Faça alguma coisa com {argumentos[1]}')
        print(f'Faça alguma coisa com {argumentos[2]}')
        print(f'Faça alguma coisa com {argumentos[3]}')
    except IndexError:
        print('Faltam argumentos')