frase = 'aaaooo'
 
# Letra maiúscula difere de minúscula em Python acentuação
i=0
apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''
#print(frase.count('o'))

while i < len(frase):
    letra_atual = frase[i]
    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_que_apareceu_mais_vezes=letra_atual
    i+=1
print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_que_apareceu_mais_vezes}" que apareceu '
    f'{apareceu_mais_vezes}x'
    )

