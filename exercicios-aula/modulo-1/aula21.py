"""
Formatação básica de strings
s - string
d - int
f - float

acrescenta caracteres pra esquerda, centro ou direita

= - força o numero aparecer antes dos zeros

Conversion flags - !r !s !a    
"""

variavel = 'ABC'
print(f'{variavel: >10}')
print(f'{variavel: ^10}')
print(f'{variavel:-<10}')
print(f'{100000.123123213213:0=+,.1f}') # o + mostra se for positivo ou negativo com esse +
print(f'O hexadecimal de 1500 é {1500:08x}')