"""
Flag - marca um local
None = sem valor
is e is not = é ou não é
id = identidade

"""

v1 = 'a'
v2 = 'a' 
print(id(v1)) #apontam para o msm ID
print(id(v2))


'''
if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)
'''

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no if')

