'''
Fatiamento de strings

0123456789
Olá mundo
-987654321
Fatiamento [i:f:p] [::]

#len fala o tamanho do array
'''

variavel ='Olá mundo'
print(variavel[4:8]) #sempre que quiser o final, pega um a mais doq vc quer

print(len(variavel))

print(variavel[0:9:4]) #esse passo no final :3 conta de qnts ele vai pular, vai de 0 até 9 contando de 2em2
print(variavel[::-1]) #inverte a string
print(variavel[-1:-10:-1]) #usa a msm ideia da linha 17 mas começa e termina em posições diferentes para indices negativos