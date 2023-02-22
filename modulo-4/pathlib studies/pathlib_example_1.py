from pathlib import Path
#caminho_projeto = Path()
#print(caminho_projeto.absolute())

# caminho_arquivo = Path(__file__)



#print(caminho_arquivo)

#print(caminho_arquivo.parent)
#print(caminho_arquivo.parent.parent)

#ideias = caminho_arquivo.parent / 'ideias' / 'arquivo.txt'  #essa barra 
#serve pra vc indicar o diretório especifico
#ele gera novos caminhos, n salvam eles, ficam apenas na memória

#print(ideias)

#arquivo = Path.home() / 'Downloads' / 'arquivo.txt'

# arquivo.touch() #ele salva o arquivo, agr o arquivo existe
# print(arquivo) 
# arquivo.write_text('eae') #cria o arquivo
# print(arquivo.read_text())
#arquivo.unlink()  apaga o arquivo

# with caminho_arquivo.open('a+') as file: #ele já abre e fecha o arquivo
#     file.write('Uma linha\n') 
#     file.write('Outra linha\n')
# print(caminho_arquivo.read_text())
# caminho_arquivo = Path.home() /'EXEMPLO'/'texto.txt'

# caminho_arquivo.touch()
# caminho_arquivo.write_text('Olá mundo')
# caminho_arquivo.unlink()

caminho_pastinha = Path.home()  /'Downloads' /'Pastinha'
caminho_pastinha.mkdir(exist_ok=True)
subpasta = caminho_pastinha / 'subpasta'
subpasta.mkdir(exist_ok = True)

outro_arquivo = subpasta / 'arquivo.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Hey')

mais_arquivo = subpasta / 'arquivo.txt'
mais_arquivo.touch()
mais_arquivo.write_text('Hey')

#caminho_pastinha.rdmir() #n da para apagar a pasta dessa forma, deve ser recurs


files = caminho_pastinha / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file_{i}.txt'
    file.touch()
    if files.exists ():        #is_file, is_dir or exists
        file.unlink()
    else:
        file.touch()

    with file.open('a+') as text_file:
        text_file.write('Olá mundo\n')
        text_file.write(f'file_{i}.txt')

def rmtree(root, remove_root=True): #recebe um caminho e itera sobre a pasta
    for file in root.glob('*'):
        if file.is_dir():
            print('DIR:', file)
            rmtree(file) #excluir uma árvore de diretório inteira
            file.rmdir()
        else:
            file.unlink()
    if remove_root:     #remove pasta
       root.rmdir()

rmtree(caminho_pastinha)