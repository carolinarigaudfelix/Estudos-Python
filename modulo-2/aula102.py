#Exercício - adiando execução de funções
def soma(x):
    def adicao(y):
        return x + y
    yield adicao

def multiplica(x):
    def multiplicador(y):
        return x * y
    yield multiplicador

def executa(funcao, * args):
    return next (funcao(*args))


soma_com_cinco = executa(soma,5)
print(soma_com_cinco(4))

multiplica_por_dez = executa(multiplica, 10)
print(multiplica_por_dez(2))