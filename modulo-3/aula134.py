"""
@property + @setter - getter e setter no modo Python
- como getter

    p/ evitar quebrar código cliente
    p/ habilitar setter
    p/ executar ações ao obter um atributo

    #Atributos que começam com _ ou __ não devem ser usados fora da classe
"""

class Caneta:
    def __init__(self, cor):
        self._cor = cor
        #private protected 
        # self._cor = self.cor #essa cor n deve ser usada, n usa esse atributo, é uma convenção
        self._cor_tampa = None

    @property
    def cor(self):
        print('Estou no getter')
        return self._cor

    @cor.setter
    def cor(self, valor): #setter tb é um método, recebe self, mas tem q receber um valor
        # if valor == 'Rosa':
        #     raise ValueError('Não aceito essa cor')
        print('Estou no Setter')
        self._cor = valor


    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta('Azul')
caneta.cor = 'Pink'
caneta.cor_tampa = 'Azul'

print(caneta.cor)
print(caneta.cor_tampa)
#getter -> obter valor

