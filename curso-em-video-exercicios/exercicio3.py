"""
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.


"""

def square_sum(numbers):
    i=0
    resultado = 0
    tamanho = len(numbers)
    for i in range(tamanho):
        resultado += numbers[i] **2
        i+=1
    return resultado

numb = [1, 2]

