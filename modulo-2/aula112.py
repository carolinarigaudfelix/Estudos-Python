#groupby - agrupando valores (itertools)
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'Joana', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'Carolina', 'nota': 'A'},
    {'nome': 'Gabriel', 'nota': 'C'},
]

# alunos = ['a','a','a', 'b', 'c'] #os dados precisam estar ordenados para ele poder agrupar
#caso contrário ele considera como outro numero, usamos sorted

def ordena(aluno):
    return aluno['nota']
    
alunos_agrupados = sorted(alunos, key=ordena)

# for aluno in alunos_agrupados:
#     print(aluno)

grupos = groupby(alunos_agrupados, key=ordena)


for chave, grupo in grupos: #separou em chave e grupo, vc escolhe ql printa
    print(chave)
    print(list(grupo))
    for aluno in grupo:
        print(aluno)