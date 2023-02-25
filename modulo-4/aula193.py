#thread faz vários processos simultaneamente
from time import sleep
from threading import Thread
from threading import Lock
"""
class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()  #inicializar o incio da propria thread

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuThread('Thread 1', 2) #obrigatoriamente tem q mandar um texto e um tempo
#depois de 5s manda isso independente do for anterior
t1.start()

t2 = MeuThread('Thread 2', 3)
t2.start()

t3 = MeuThread('Thread 3', 5)
t3.start()
for i in range(20):
    print(i)
    sleep(1)
"""
###############################################################################
"""
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)

t1 = Thread(target=vai_demorar, args=('Olá mundo 1', 10))
t1.start()

t1.join() #o codigo principal espera pra fazer qlqr coisa
a thread principal espera ela acabar pra executar isso



 t2 = Thread(target=vai_demorar, args=('Olá mundo 2', 10))
 t2.start()

 t3 = Thread(target=vai_demorar, args=('Olá mundo 3', 5))
 t3.start()

while t1.is_alive(): #serve pra esperar a thread
    print('Esperando ela')
    sleep(2)

print('Thread acabou!')

 for i in range(10):
     print(i)
     sleep(.5)
"""

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock() #tranca o método

    def comprar(self, quantidade):
        self.lock.acquire()
        if self.estoque < quantidade:
            print("sem ingressos suficientes")
            self.lock.release()
            return
        
        sleep(1)
        self.estoque -= quantidade

        print(f'Você comprou {quantidade} ingressos, temos {self.estoque}')
        self.lock.release()

if __name__ == '__main__':
    ingressos = Ingressos(10)
    for i in range(1,20):
        t = Thread(target = ingressos.comprar, args=(i,))
        t.start()
    print(ingressos.estoque)