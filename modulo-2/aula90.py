#dir, hasattr e getattr em Python

#dir mostra todos os nomes definidos dentro de string
#hasattr checka se o atributo existe
#getattr checka se um determinado método tem um nome la dentro ex: upper
string = 'Carol'
metodo='upper'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string,metodo)())
    #print(string.upper())
else:
    print('Não existe método', metodo)