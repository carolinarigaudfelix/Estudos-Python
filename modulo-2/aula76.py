"""
Sets - Conjuntos em Python (tipo set)
Conjuntos são ensinados na matemática
Representados graficamente pelo diagrama de Venn
Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.

Criando um set
set(iterável) ou {1, 2, 3}
"""

#Sets são eficientes para remover valores duplicados de iteráveis
"""
-Seus valores sempre serão únicos
-Não aceitam valoers mutáveis
Eles não tem índexes;
eles não garantem ordem;
eles são iterávies (for, in, not, in)

Métodos úteis:
add, update, clear, discard
"""

# s1 = set('Luiz')#só tem valor, n tem par de chave e valor
# s1 = {'Luiz', 1, 2, 3}
# print(s1)

# s1 = {1, 2, 3, 3, 3, 3, 3, 1} #set elimina automaticamente numeros e valores duplicados mas eles não garantem a ordem
# print(s1)

# s1 = s1 = {1, 2, 3, 4, (123,)} #tupla precisa de virgula no final, valores mutaveis n entram em sets
# print(s1)

s1 = {1, 2, 3}
print(3 in s1)
for numero in s1:
    print(numero)

#Métodos úteis
s1 = set()
s1.add('luiz')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4))# pra passar uma frase manda um iterável em si
print(s1)
#s1.clear()
s1.discard('Olá mundo')
s1.discard('Luiz')
print(s1)



