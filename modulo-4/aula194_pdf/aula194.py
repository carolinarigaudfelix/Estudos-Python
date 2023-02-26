# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2

from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter, PdfMerger
PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20.pdf'
PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

# for page in reader.pages:
#     print(page)
#     print()

page0 = reader.pages[0]
imagem0 = page0.images[0]

print(page0.extract_text())
with open(PASTA_NOVA / imagem0.name, 'wb') as fp:
    fp.write(imagem0.data)

writer = PdfWriter()
# writer.add_page(page0)

with open(PASTA_NOVA / 'NOVO_PDF.pdf' , 'wb') as arquivo: #joga em 2 páginas
    for page in reader.pages:                              #do mesmo pdf
        writer.add_page(page)
    writer.write(arquivo)

#agora para por em 2 cpfs separados

for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f'page{i}.pdf' , 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)

# for page in reader.pages:
#     print(page)
#     print()

# with open(PASTA_NOVA / 'page0.pdf', 'wb') as arquivo:
#     writer.write(arquivo)  #escreve os dados no arquivo

merger = PdfMerger
#nesse caso os nomes importam
files = [
    PASTA_NOVA / f'page1.pdf',
    PASTA_NOVA /'page0.pdf',
]
merger = PdfMerger()
for file in files:          #inverte a ordem do pdf
    merger.append(file)

with open(PASTA_NOVA / 'MERGED.pdf', 'wb') as arquivo:
    merger.write(arquivo)
