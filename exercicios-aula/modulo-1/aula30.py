#documentação, tipos imutáveis, métodos

string = 'carol'
#string[3] = 'ABC' não da pra fazer mudanças em str, int, float e bool, eles são objetos que tem ações próprias
#str.capitalize() isupper, etc
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(outra_variavel)
print(string.capitalize())