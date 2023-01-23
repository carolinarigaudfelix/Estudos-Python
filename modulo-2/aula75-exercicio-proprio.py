

# perguntas = [
#     {
#         'Pergunta': 'Quanto é 2+2?',
#         'Opções': ['1', '3', '4', '5'],
#         'Resposta': '4',
#     },
#     {
#         'Pergunta': 'Quanto é 5*5?',
#         'Opções': ['25', '55', '10', '51'],
#         'Resposta': '25',
#     },                                                                  #Aqui tem um dicionário com um conjunto de listas
#     {
#         'Pergunta': 'Quanto é 10/2?',
#         'Opções': ['4', '5', '2', '1'],
#         'Resposta': '5',
#     },
# ]

# qtd_acertos = 0
# for pergunta in perguntas:
#     print('Pergunta:', pergunta['Pergunta'])  #pergunta armazena todas as Perguntas do dicionário
#     print()

#     opcoes = pergunta['Opções'] #opções armazena todas as opções do dicionário
#     for i, opcao in enumerate(opcoes):
#         print(f'{i})', opcao) #o i serve pra mostrar o indice e o enumerate enumera esses indices
#     print()

#     escolha = input('Escolha uma opção: ')#usuario insere uma opção

#     acertou = False
#     escolha_int = None
#     qtd_opcoes = len(opcoes)
 
#     if escolha.isdigit(): #checka se é um número e converte pra inteiro
#         escolha_int = int(escolha)

#     if escolha_int is not None:
#         if escolha_int >= 0 and escolha_int < qtd_opcoes:
#             if opcoes[escolha_int] == pergunta['Resposta']:
#                 acertou = True

#     print()
#     if acertou:
#         qtd_acertos += 1
#         print('Acertou 👍')
#     else:
#         print('Errou ❌')

#     print()


# print('Você acertou', qtd_acertos)
# print('de', len(perguntas), 'perguntas.')




#faça um exercício pra conferir informações pessoais

perguntas= [
    {
        'Pergunta': 'Qual é a minha cor favorita?',
        'Opções': ['Azul', 'Roxo', 'Amarelo', 'Verde'],
        'Resposta': 'Roxo',  
    },
    {
        'Pergunta': 'Qual comida eu mais gosto?',
        'Opções': ['Sushi', 'Hamburguer', 'Lasanha', 'Strogonoff'],
        'Resposta': 'Strogonoff',  

    },
    {
        'Pergunta': 'Qual o meu anime favorito?',
        'Opções': ['FMA', 'AOT', 'SWKNU', 'OP'],
        'Resposta': 'FMA', 
    }, 
        
]

qtd_acertos = 0

for pergunta in perguntas:
    print(f'Pergunta: ', pergunta['Pergunta'])
    print()
    opcoes= pergunta['Opções']
    
    for i, opcao in enumerate(opcoes):  #enumerate precisa de 2 parametros
        print(f'{i})', opcao)

    escolha = input("Insira uma opção: ")

    #coisas que devem ser checkadas: se é um int, se é um número, se acertou

    if escolha.isdigit:
        escolha_int = int(escolha)
        if escolha_int is not None:
            if escolha_int >=0 and escolha_int<len(opcoes):
                if opcoes[escolha_int] == pergunta['Resposta']:
                    acertou = True
                    print('Parabens, você acertou')
                    qtd_acertos+=1
                else:
                    print('Ops, resposta errada...')
print(f'Você acertou essa quantidade: {qtd_acertos}')