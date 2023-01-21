"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo código é alcançavel
O escopo local é o escopo onde apenas nomes do mesmo local 
podem ser alcançados.
"""

#o que estiver mais interno é chamado
x=1

def escopo():
    x=10

    def outra_funcao():
        x=11#se comentar esse x, o print a seguir pega o último x mais próximo ao escopo
        y=2
        print(x, y)
   
    outra_funcao()
    print(x)

escopo()

