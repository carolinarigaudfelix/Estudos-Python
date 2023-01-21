'''
-Pedir um numero inteiro
-Dizer se é impar ou par
-Dizer se é inteiro

-Pedir a hora
-Dizer: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23

-Peça o primeiro nome do usuário
-se o nome tiver 4 letras ou menos escrever "Seu nome é curto"
-se o nome tiver entre 5 e 6 letras, escreva "Seu nome é normal"
-Se o nome tiver mais que 6 letras, escreva "Seu nome é muito grande"
'''

#1 código

"""
Solução

entrada = input('Digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0

    if par_impar:
        par_impar_texto = ''

    print(f'O número {entrada_int} é {}')
else:
    print('Você não digitou um número inteiro")
"""


numero = float(input('Insira um numero: '))
resto = numero % 2
inteiro = numero % 1

print(numero)
print(resto)

if resto==0 and inteiro==0:
    print("Esse número é par e inteiro")
elif resto!=0 and inteiro==0:
    print("Esse número é ímpar e inteiro")
elif resto==0 and inteiro!=0:
    print("Esse número é par mas não é inteiro")
elif resto!=0 and inteiro!=0:
    print("Esse número é ímpar e não é inteiro")

