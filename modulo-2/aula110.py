# count é um iterador sem fim
from itertools import count

c1 = count(step=10, start=8) #pode por com os argumentos nomeados ou sem
r1 = range(16, 100, 8) #aq tem um limite, vc pode estabelecer um limite tb
#o último número é os múltiplos, o primeiro é de onde começa

print(next(c1))
print(next(c1))

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

print('count')
for i in c1: #como counter é um iterador infinito ele gera um loop infinito
    if i > 100:
        break

    print(i)
print()
print('range')
for i in r1:
    if i > 100: #mas aq vc estabeleceu uma condição pra ele parar
        break   
    print(i)