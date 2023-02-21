# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar aqruivos -> os.unlink
#Mover/Renomear ->shutil.move
#Mover/Renomear -> os.rename
# Copiar -> shutil.copy
# Apagar -> os.link
# Apagar diretório recursivamente -> shutil.rmtree
# Renomear / Mover -> shutil.move ou os.rename


import os
import shutil

HOME = os.path.expanduser('~') #expande a home do usuário do computador
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'EXEMPLO')
NEW_FOLDER = os.path.join(DESKTOP, 'NEW_FOLDER')

#usar com cautela

shutil.rmtree(NEW_FOLDER, ignore_errors=True)
shutil.copytree(PASTA_ORIGINAL, NEW_FOLDER) #copia e cria
shutil.rmtree(NEW_FOLDER, ignore_errors=True) #remove a pasta




#==========================================
# os.makedirs(NEW_FOLDER, exist_ok=True)

# for root, dirs, files in os.walk(PASTA_ORIGINAL):
#     for dir_ in dirs:
#         caminnho_novo_diretorio = os.path.join(
#             root.replace(PASTA_ORIGINAL, NEW_FOLDER), dir_
#         )
#         os.makedirs(caminnho_novo_diretorio, exist_ok=True)

#     for file in files:
#         caminho_arquivo = os.path.join(root, file)
#         caminnho_novo_arquivo = os.path.join(
#             root.replace(PASTA_ORIGINAL, NEW_FOLDER), file
#         )
#         shutil.copy(caminho_arquivo, caminnho_novo_arquivo) 
#         #copia de um diretorio para o outro