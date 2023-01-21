"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valoers padrão. Caso valor não seja
enviado para o parâmetro, o valor padrão será usado.
Refatorar: editar seu código
"""

def soma(x, y, z =None):   #parametro sem valor 
    if z is not None:
        print(f'{x=} + {y=} + {z=}', 'soma', x + y +z)
    else:
         print(f'{x=} + {y=}','soma', x + y)
soma(1, 2)
soma(3, 5)
soma(100, 20)
soma(7, 9, 0)

"""
Se você declarar um parâmetro com valor padrão, todos a seguir consequentemente terão q ser valores padrões também
"""