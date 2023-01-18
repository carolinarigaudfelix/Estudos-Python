"""
Introdução ao try/except

try-> tentar executar o código
except-> ocorreu algum erro ao tentar executar
"""

# numero = input('Vou dobrar o número que você digitar: ')


# numero_float = float(numero)
# print(f'O dobro de {numero} é {numero * 2:.2f}')


numero_str = input('Vou dobrar o número que vc digitar: ')

print(numero_str.isdigit()) #is digit checka se digitou APENAS números

numero_float = float(numero_str)
print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')