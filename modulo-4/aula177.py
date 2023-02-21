"""
csv.reader e csv.DictReader
csv.reader lê o CSV em formato de lista
csv.DictReader lê o CSV em formato de dicionário
"""

import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'Folha de cálculo sem nome - aula176.csv'

with open(CAMINHO_CSV, 'r', encoding="utf-8") as arquivo:
    # leitor = csv.reader(arquivo)
    leitor = csv.DictReader(arquivo)
    
    for linha in leitor:
        print(linha['Nome'], linha['Idade'], linha['Endereço'])