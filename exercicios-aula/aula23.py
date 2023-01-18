"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:

    Exiba:
    Seu nome é {nome}  X
    Seu nome invertido é {nome invertido} x
    Se nome contém (ou não) espaços  x 
    Seu nome tem {n} letras x
    A primeira letra do seu nome é {letra} x
    A última letra do seu nome {letra} x
Se nada for digitado em nome ou idade:
    exiba "Desculpa, você deixou campos vazios."

"""

nome = input('Insira um nome ')
idade = input('Insira sua idade ')
tamanho = len(nome)


if nome and idade:
    print(f'Seu nome é {nome}')
    print(nome[::-1])
    if ' ' in nome:
        print('Seu nome contém espaços')
    print(f'O seu nome tem esse tamanho: {tamanho}')
    print(f'A última letra do seu nome é {nome[-1:]}')
    print(f'A primeira letra do seu nome é {nome[0]}')
else:
    print('Desculpa, você deixou campos vazios')





