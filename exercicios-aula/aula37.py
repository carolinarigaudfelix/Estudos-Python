"""
while/else
"""

string = 'Valorqualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':  # sempre que achar o break, laço para de ser executado e n executa else
        break

    print(letra)
    i += 1

else:
    print('Não encontrei espaço na string')
print('Fora do while.')