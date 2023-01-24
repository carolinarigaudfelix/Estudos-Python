#Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) #tem __iter__ e __next__

"""
o iterável detém os valores
o iterator só entrega um valor por vez, n sabe primeiro, tanho, nada, só o próximo
"""
print(next(iterator))
#iterator fornece o acesso a um elemento sem saber suas informações subjacentes
import sys
#se usar um next em um elemento do iterable além do índice do iterator, ele da um erro, ele só vai 
#até o último índice do iterable e para

#generator = [ n for n in range(100000)] é ruim
lista = [n for n in range(10000)]
generator = (n for n in range(10000)) #só entrega um valor por vez, n entrega tudo
print(sys.getsizeof(lista)) #esse método sys getsizeof serve para dizer o tamanho da lista em BYTES
print(sys.getsizeof(generator))

print(next(generator))
print(next(generator))
print(next(generator))

# for n in generator: não tem tamanho, n tem índice, n tem len, tem nada, n está na memória
#     print(n)