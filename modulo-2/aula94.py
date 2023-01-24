#Try, except, else e finally
# a = 18
# b = 0
# c = a/b
"""
Obviamente isso daria erro, mas se você por no try
try:
    c = a/b
ele vai efetuar a divisão e silenciar o erro, isso é uma má prática
porém, se for
try:
    a = 18  
    b = 0
    c = a/b
ele cai direto no except

é necessário informar no except qual erro você está tratando, fazendo dessa forma acima, você além de não identificar o erro
corre o risco de errar algum código


"""
try:
    a = 18
    b = [0]
    print('Linha 1'[10000])
    c = a / b
    print('Linha 2')

except ZeroDivisionError: #toda exceção é uma classe, qnd da algum erro eles dão o nome da classe pra vc tratar individualmente
    print('Dividiu por zero.')
except NameError:
    print('Nome b não está definido')

except (TypeError, IndexError) as error: #pra tratar mais de um erro basta considerar uma tupla 
    print('TypeError + IndexError')# o ideal é tratar erros individualmente
    print('MSG:', error)
    print('Nome', error.__class__.__name__)
except Exception: #except acima de todas as except, trata qualquer erro do programa não é indicado
    print('Erro Desconhecido.') 

print('Continuar')