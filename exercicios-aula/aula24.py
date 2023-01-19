"""
Introdução ao try/except

try-> tentar executar o código
except-> ocorreu algum erro ao tentar executar
"""
# numero = input('Vou dobrar o número que você digitar: ')


# numero_float = float(numero)
# print(f'O dobro de {numero} é {numero * 2:.2f}')

numero_str = input('Vou dobrar o número que vc digitar: ')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}') #is digit checka se digitou APENAS números
except:
    print('Isso não é um número')


'''
if numero_str.isdigit():
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}') #is digit checka se digitou APENAS números
else:
    print('Isso não é um número')

'''

