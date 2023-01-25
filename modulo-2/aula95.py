# try, except, else e finally
#finally sempre será executado
try:
    print('Abrir Arquivo')
    #8/0
except ZeroDivisionError:
    print('Dividiu zero')
except NameError as error: 
    print('Name error')
    print(error.__class__.__name__)
else:
    print('Não deu erro') #else do except
finally:
    print('Fechar Arquivo')

    #try n pode ficar sozinho, except n vem sozinho nem else, nem finallly
    #try except, try except finally ou try except else finally