#FOR

texto = 'Python'
novo_texto = ''

for letra in texto: # para cada letra em iteravel, exiba na tela, letra é só uma variável, in vai percorrer o for
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto)
