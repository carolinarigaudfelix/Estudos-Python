"""
-Peça o primeiro nome do usuário
-se o nome tiver 4 letras ou menos escrever "Seu nome é curto"
-se o nome tiver entre 5 e 6 letras, escreva "Seu nome é normal"
-Se o nome tiver mais que 6 letras, escreva "Seu nome é muito grande"
"""

nome = input('Insira o seu primeiro nome: ')
tamanho = len(nome)

if tamanho >=1:
    if tamanho <=4:
        print('O seu nome é muito curto!')
    elif tamanho >=5 and tamanho<=6:
        print('Seu nome é normal!')
    elif tamanho>6:
        print('O seu nome é muito grande!')
