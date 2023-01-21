"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o (valor)
"""

def soma (x, y, z):
    #Definição
    print(f'{x=} y={y} z={z}', '|', 'x + y + z', x + y + z)


#se nomear algum parametro, todos precisam ser nomeados
#ex: soma(x=1,y=2,z=3)
#argumento é o valor q passa pra variável
soma(1, 2, 3, sep='-') 
#a ordem dos fatores importa
