"""
Interpretador do Python

python mod.py (executa o mod)
python -u (unbuffered)
python -m mod (lib mod como script)
python -c 'cmd' (comando)
python -i mod.py (interativo com mod)
python -c 'cmd' (comando)
python -i mod.py (interativo com mod)

"""


#DESEMPACOTAMENTO EM CHAMADAS
# DE MÉTODOS E FUNÇÕES

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

# p, b, *_, ap, u = lista
# print(p, u, ap)

# for nome in lista:
#     print(nome, end=' ', sep=' ')

print(*lista) #separa um por um com o asterisco
print(string)
print(*string, end='\n')
