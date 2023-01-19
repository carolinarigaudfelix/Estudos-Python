#-Pedir a hora
#-Dizer: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23

"""
Solução

entrada = input('Digite a hora em números inteiros: ')

try:
    hora= int(entrada)
    if hora>=0 and hora<=11:
        print('Bom dia)
    elif hora>=12 and hora <=17:
        print('Boa tarde')
    elif hora >= 19 and <=23:
        print('Boa noite')
    else:
        print(Não conheço essa hora)
except:
    print("Por favor digite um número inteiro)
"""

hora = int(input('Que horas são? '))
minuto = int(input('Quantos minutos? '))
DIA = 11
TARDE = 17
NOITE = 23
MAX_HORA=23
MAX_MINUTO=59

if hora <=MAX_HORA and minuto <=MAX_MINUTO:
    if hora<=DIA:
        print(f'Bom dia {hora}:{minuto}')
    elif hora >DIA and hora<NOITE:
        print(f'Boa tarde {hora}:{minuto}')
    elif hora>TARDE:
        print(f'Boa noite {hora}:{minuto}')
