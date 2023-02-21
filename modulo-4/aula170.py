#os.listdir para navegar em caminhos
import os
#C:\Users\carol\OneDrive\Área de Trabalho\EXEMPLO
caminho = os.path.join('\\Users','carol', 'OneDrive', 'Área de Trabalho', 'EXEMPLO')


for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta): #verifica se o caminho existe
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print('  ', imagem)
