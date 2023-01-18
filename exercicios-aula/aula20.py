"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal(ABCDEF0123456789)   -> %x para hexadecimal em minusculo, %X para hexadecimal em maiúsculo

"""

nome='Carolina'
preco= 100.000
variavel = '%s, o preço é R$%.1f'  % (nome, preco) #essa "%" é para interpolação, se for só uma variável, sem parenteses

print(variavel)

print('O hexadecimal de  %d é %04x' % (15,15))

#interpolação, f string ou format


