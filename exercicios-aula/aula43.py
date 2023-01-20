"""
Faça um jogo para o usuário adivinhar qual é a palavra secreta

Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar
apenas uma letra. 

qual o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    -Se a letra digitada estiver na palavra secreta, exiba a letra
    -Senão, exiba *
-Faça a contagem de tentativas do usuário

"""

#Solução
palavra_secreta = 'perfume'
letras_acertadas = ''
tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    tentativas += 1
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra. ')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
        
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada: ', palavra_formada)    

    if palavra_formada == palavra_secreta:
        print('VOCE GANHOU PARABENS')
        print(f' A palavra secreta era {palavra_secreta}')
        print('Tentativas: ', tentativas)
# =

# encontrada = ''
# contagem = 0
# while secreta !=encontrada:
#     for i in range(tamanho):
#         pergunta = input('Diga uma letra dessa palavra:')
#         if pergunta in secreta:
#             print(f'Você acertou uma letra! {pergunta}')
#             encontrada += pergunta
#             print(encontrada)
#             contagem +=1
#         else:
#             print('*')
#             contagem +=1
# print(f'Seu total de tentativas foi: {contagem}')