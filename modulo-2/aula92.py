#Introdução às Generator functions em Python
# generator = (n for n in range(1000))
#todo generator é um iterator

#def generator(n=0):
#     yield 1         #Pausar
#     print('Continuando')
#     yield 2
#     print('Mais uma...')
#     yield 3
#     print('Vou terminar')
#     return 'Acabou'

def generator(n=0, maximum=10):
    while True:
        yield n
        n +=1
        if n>maximum:
        
            return


gen = generator(n=0, maximum=9)
for n in gen:
    print(n)
# print(next(gen))
# print(next(gen))
# print(next(gen))


#return retorna e para, generator pausa