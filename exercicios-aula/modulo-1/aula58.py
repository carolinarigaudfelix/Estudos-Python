"""
CPF:746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma contagem regressiva começando de 10


Ex: 746.824.890-70 (74682489070)
    10 9 8 7 6 5 4 3 2
     7 4 6 8 2 4 8 9 0
   70 36 48 56 12 20 32 27 0

   Somar todos os resultados:
   70+36+48+56+12+20+32+27+0=301

   Multiplicar o resultado anterior por 10
   301*10 = 3010

   Obter o resto da divisão da conta anterior por 11
   3010 % 11 = 7
   Se o resultado for maior que 9:
   o resultado é 0
   caso contrário o resultado é
"""

cpf = '746.824.890'.replace('.', '')
cpf_enviado_usuario =[]
cpf_com_digito = '74682489070'
tamanho = len(cpf)
tamanho_2 = len(cpf_com_digito)
indice = 0
cpf_sem_ponto = []
multiplicacao = []
multiplicacao_2= []
fator=10
soma=0
 
while indice<tamanho_2:
  if(cpf_com_digito[indice] == '-' or cpf_com_digito[indice] == '.'):
    print('Removendo pontuação porra')
  else:
   cpf_enviado_usuario+=cpf_com_digito[indice]
  indice+=1
print(f'CPF enviado pelo usuário{cpf_enviado_usuario}')

indice=0

while indice<tamanho:
  if(cpf[indice] == '-' or cpf[indice] == '.'):
    print('Removendo pontuação')
  else:
    cpf_sem_ponto+=cpf[indice]
  indice+=1
print(f'CPF sem ponto:{cpf_sem_ponto}')
indice = 0
inteiro = ['']

inteiro = [int(i) for i in cpf_sem_ponto]   #conversão lista de int 

while indice<tamanho:
  if inteiro[indice:] == 0:
    del inteiro[indice]
  indice+=1

digito_1=''
indice=0

for i in range(0, 9):
  multiplicacao.append(inteiro[i]*fator)
  soma+=(multiplicacao[i]*10)
  fator-=1

digito_1 = soma%11

if(digito_1 >9):
  print('O resultado é 0')
else:
  print(f'O resultado do primeiro digito é {digito_1}')

#agora para saber o segundo dígito
inteiro.append(digito_1)

fator=11
soma_2=0

for i in range(0, 10):
  multiplicacao_2.append(inteiro[i]*fator)
  soma_2+=(multiplicacao_2[i]*10)
  fator-=1

digito_2 = soma_2%11

if(digito_2 >9):
  print('O resultado do segundo digito é 0')
else:
  print(f'O resultado do segundo digito é {digito_2}')
inteiro.append(digito_2)

cpf_sem_ponto.append(str(digito_1))
cpf_sem_ponto.append(str(digito_2))
novo_cpf = cpf_sem_ponto


novo_cpf = [int(i) for i in cpf_sem_ponto]  

cpf_enviado_usuario = [int(i) for i in cpf_enviado_usuario]  

if inteiro == cpf_enviado_usuario:
    print(f'{inteiro} é válido')
else:
    print('CPF inválido')

#Solução
"""
cpf='746.824.890-70'
nove_digios = cpf[:9]

contdor_regressivo_1 = 10

for digito in nove_digitos:
  print(digito)
  resultado_digito1 += (int(digito) * contador_regressivo_1)
  contador_regressivo_1 -=1
digito = (resultado_digito_1 * 10) % 11
digito_1 = digito if digito <= 9 else 0
print(digito_1)
)
"""