"""
Faça uma lista de comprar com listas
o usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa com erros de índices inexistentes na lista
"""
opcao=''
lista = []
indice = ''
lista_enumerada = enumerate(lista)

while opcao !='s':
    opcao = input('Selecione uma opção: [i]nserir [a]pagar [l]istar:')  

    if opcao =='i':
            valor = input('Insira o nome do item: ')
            lista.append(valor)


    if opcao =='a':
        tamanho = len(lista)
        indice =int(input('Qual o índice que deseja apagar?'))

        print(tamanho)
        print(indice)
        print(lista)
        if indice <=tamanho:
           del(lista[indice])
        elif indice>tamanho:
            print('Por favor, Insira um indice valido')
        

    if opcao =='l':
        for i,produto in lista_enumerada:
            print(i,produto)
    if(opcao != 'i' and opcao!='a' and opcao!='l' and opcao!='s'):
        print('Por favor listar opção válida.')

#OBS: da pra usar except ValueError na parte de apagar para printar para por outro numero no indice q seja valido