
import json
from aula129_a import CAMINHO_ARQUIVO, Pessoa, fazer_dump
novos_dados = ['']

fazer_dump()
with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
        novos_dados = json.load(arquivo)
        p1 = Pessoa(**novos_dados[0])
        p2 = Pessoa(**novos_dados[1])
        p3 = Pessoa(**novos_dados[2])
       

        print(p1.nome, p1.idade)
        print(p2.nome, p2.idade)
        print(p3.nome, p3.idade)


