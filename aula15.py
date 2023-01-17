#operadores
#>      >=      <     <=     ==     !=     

valor1 = (input('Digite um valor: '))
valor2 = (input('Digite outro valor: '))

primeiro_valor = (valor1)
segundo_valor = (valor2)

if primeiro_valor > segundo_valor:
    print('O numero:', primeiro_valor, 'é maior que o número:'  ,segundo_valor)

elif primeiro_valor < segundo_valor:
    print('O numero:',  primeiro_valor,  'é menor que o número:'  ,segundo_valor)

else:
    print('Eles são iguais')
