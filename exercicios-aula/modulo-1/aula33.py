#laços de repetição

contador =0

while contador <=100:
    contador += 1

    if contador == 6:
        print('Nao vou mostrar o 6')
        continue   # qnd a expressão for verdadeira ele volta pro começo do laço

    print(contador)
    
    if contador >=10 and contador <=27:
        print('Nao vou mostrar o', contador)
        continue


    
