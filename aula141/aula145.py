"""
Criando Exceptions em Python Orientando a Objetos
Para criar uma Exception em Python, você só
precisa herdar de alguma exceção da linguagem.
A recomendação da doc é herdar de Exception.
Criando exceções (comum colocar Error ao final)
Levantando (raise) / Lançando (throw) exceções
Relançando exceções
Adicionando notas em exceção (3.11.0)
"""
class MeuError(Exception):
    ...
    

class OutroError(Exception):
    ...

def levantar():
    exception_ = MeuError('a', 'b', 'c')
    exception_.add_note('Olha a nota 1')
    exception_.add_note('Vc errou isso')
    raise exception_

try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    exception_ = OutroError('Vou lançar de novo')
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('Mais uma nota')
    raise exception_ from error

