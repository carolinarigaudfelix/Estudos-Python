"""
@property - um getter no modo Pythônico
getter - um método para obter um atributo
cor -> get_cor()
modo pythônico - modo do Python fazer coisas
@property é uma propriedade do objeto, ela é um método que
se comporta como um atributo

Geralmente é usada nas seguintes situações:
- como getter
- p/evitar quebrar código cliente
- p/ habilitar setter
- p/executar ações ao obter um atributo


Código Cliente - é o código que usa o seu código
"""

class Caneta:
    def __init__(self, cor):
        #private    protected    public
        self.cor_tinta = cor

    @property
    def cor(self): #método
        print('Property')
        return self.cor_tinta

    @property
    def cor_tampa(self):
        return 123456

###############################

caneta = Caneta("Azul") # o programa que usa a classe é o código do cliente
print(caneta.cor) #atributo
print(caneta.cor_tampa)
##################################

# class Caneta:
#     def __init__(self, cor):
#         #private    protected    public
#         self.cor_tinta = cor

#     def get_cor(self):
#         print('Get Cor')
#         return self.cor_tinta