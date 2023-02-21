"""
csv.reader e csv.DictReader
csv.reader lê o CSV em formato de lista
csv.DictReader lê o CSV em formato de dicionário
"""
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula178.csv'

lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

with open(CAMINHO_CSV, 'w', encoding="utf-8") as arquivo:
    #nome_colunas = lista_clientes[0].keys()
    #nome_colunas = ['Nome', 'Endereço'] 
    nome_colunas = lista_clientes[0].keys()
    
    #escritor = csv.writer(arquivo)
    #escritor.writerow(nome_colunas)
    escritor = csv.DictWriter( #escreve nos arquivos, tem que especificar o
        #cabeçalho
        arquivo, 
        fieldnames=nome_colunas #nome dos campos
    )
    escritor.writeheader() 
    #escreve o topo do arquivo
    for cliente in lista_clientes:
        print(cliente)
        escritor.writerow(cliente)
    # for cliente in lista_clientes:
    #     #print(cliente.values)
    #     escritor.writerow(cliente)

#print(lista_clientes[0].keys()) #mostra as colunas
