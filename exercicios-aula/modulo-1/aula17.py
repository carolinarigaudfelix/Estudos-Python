
"""
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if(entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

"""

print (True or False or 0 or 'abc') #primeira vez que achar um valor verdadeiro vai retornar verdadeiro

senha = input('Senha:') or 'Sem senha'
print(senha)