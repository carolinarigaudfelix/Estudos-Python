"""
Método especial __call__
callable é algo que pode ser executado com parênteses
Em calsses normais, __call__ faz a instância de uma classe "callable"

"""
class CallMe:
    def __init__(self, phone):
        self.phone = phone
    
    def __call__(self, nome):
        print(nome, 'está Chamando,', self.phone)
        return 1234
    
call1 = CallMe('123456789')
retorno = call1('Carol')
print(retorno)