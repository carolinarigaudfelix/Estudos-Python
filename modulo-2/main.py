import os

caminho_arquivo = 'C:\\Users\\carol\\OneDrive\\Área de Trabalho\\Estudos-Python\\modulo-2\\EncodeTest'
caminho_arquivo = 'aula119.txt'

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha1\n')
    arquivo.write('Linha2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha4\n')
    )

#os.remove(caminho_arquivo) ambos apagam o arquivo
#os.unlink(caminho_arquivo)
# os.rename(caminho_arquivo, 'aula119-2.txt')