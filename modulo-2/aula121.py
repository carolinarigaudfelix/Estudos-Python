#criar tarefas, desfazer e refazer a ação
#Exercício - Lista de tarefas com desfazer e refazer
"""
todo = [] -> lista de tarefas
todo = ['fazer café'] -> adicionar fazer café
todo = ['fazer café', 'caminhar'] - > adiciona caminhar
desfazer = ['fazer café,] -> Refazer ['caminhar']
desfazer = [] -> Refazer ['caminhar', 'fazer café']
refazer = todo ['fazer café']
refazer = todo ['fazer café', 'caminhar']
"""
#listar, desfazer, refazer, adicionar

import json

def adiciona_tarefa(nome,lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

lista = []
acao = ''
while acao != 'S':
    acao = input('[L]istar, [D]esfazer, [R]efazer, [A]dicionar ou [S]air?')
    if acao in 'Aa':
        nova_tarefa = input('Insira o nome da tarefa: ')
        tarefa = adiciona_tarefa(nova_tarefa,lista)
        with open('tarefas.json', 'w', encoding='utf8') as arquivo:
            json.dump(
                tarefa,
                arquivo,
                ensure_ascii=False,
                indent=2
            )
    elif acao in 'Ll':
        for item in tarefa:
            print(f'A lista é:\n{item}')
    elif acao in 'Dd':

        with open('deleted.json', 'w', encoding='utf8') as arquivo:
            json.dump(
                tarefa[-1],
                arquivo,
                ensure_ascii=False,
                indent=2
            )
        tarefa.pop()
    elif acao in 'Rr':
        with open('deleted.json', 'r', encoding='utf8') as arquivo:
            tarefa.append(json.load(arquivo))