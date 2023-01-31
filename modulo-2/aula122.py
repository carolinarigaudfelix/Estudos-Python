"""
Controlando a quantidade de argumentos posicionais e nomeados em funções
*args (ilimitado de argumentos posicionais)
**kwargs (ilimitado de argumentos nomeados)
Positional - only Parameters (/) - Tudo antes da barra deve
ser !apenas! posicional
PEP 570 - Python Positional-Only Parameters

Kyword-Only arguments (*) - * sozinho !Não pega! valores.
PEP 3102 - Keyword-Only Arguments
"""

# def soma(a, b, /, x, y): #tudo que vem antes da barra só pode ser posicional
def soma(a, b,/, *, c, **kwargs): 
    #tudo q vier antes do asterisco é argumento posicional, 
    #depois, argumento nomeado, logo n deve ser chamado como posicional
    print(kwargs)
    print(a + b + c)

# soma(x=1, y=2) 
soma(1, 2, c=3, nome='teste')