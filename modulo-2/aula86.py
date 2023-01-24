lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))#tupla aceita mais de um valor, n da pra por 2 valores no msm indice, ent usamos tupla
lista = [
    (x, y) 
    for x in range(3) #x da esquerda é oq vai ser incluido na lista nova
    for y in range(3)
]

lista = [
    [letra for letra in 'Luiz']
    # [x for y in range(3)] # para cada x vc faz uma nova list comprehension
    for x in range(3)
]
print(lista)
