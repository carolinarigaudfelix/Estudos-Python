"""
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next>me entrega o proximo valor
iter ->entrega seu iterador
"""

texto = iter('Luiz')
iteratador = iter(texto)
print(texto)
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))


while True:
    try:
        letra = print(next(iteratador))
        print(letra)
    except StopIteration:
        break