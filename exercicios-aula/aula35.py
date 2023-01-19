"""
Iterando Strings com While
"""
       #012345678910111213
# nome = "Carolina Felix" #iteráveis

# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)

# print(nome[4])

# nova_String +='*C*A*'...




nome = input('Insira o seu nome: ')
tamanho = len(nome)
i = 0
novo_nome = ''

# while i <tamanho:
#        novo_nome = f'{nome[:i] + "*"}'         #tá errado por não ter separado letra por letra para fazer as operações.
#        print(f'{novo_nome}')
#        i+=1                                                          #TENTATIVA

#        #outra_variavel = f'{string[:3]}ABC{string[4:]}'

#solução
while i < tamanho:
       letra = nome[i]
       novo_nome += f'{letra}*'
       i += 1

print(novo_nome)
