#Dictionary Comprehension e Set Comprehension

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

for chave, valor in produto.items():
    print(chave, valor)

dc = {
    chave: valor  
    if isinstance(valor, (int, float)) else  valor.upper() #se o valor for uma instância de int ou float, apresenta o valor
    #do contrário, põe string em letra maiúscula
    for chave, valor 
    in produto.items()
    if chave == 'categoria' #esse if é um filtro pra incluir somente categoria, se for != 'categoria, mostra os outros.
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('c', 'valor a'),
]
# dc = {
#     chave: valor
#     for chave, valor in lista
# }
print(dict(lista)) #transforma a lista em dict pq tem par chave e valor

s1 = {i ** 2 for i in range(10) if i==4}
print(s1)