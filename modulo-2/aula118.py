"""
Criando arquivos com Python
Usamos a função open para abrir
Um arquivo em Python (ele pode ou não existir)
Modos:
r (leitura), w (escrita), x (para criação)
a (escreve ao final), b (binário)
t (modo texto), + (leitura e escrita)
Context manager - with (abre e fecha)
Métodos úteis
write, read (escrever e ler)
writelines (escrever várias linhas)
seek (move o cursor)
readline (ler linha)
readlines (ler linhas)
Vamos falar mais sobre o módulo os, mas:
os.remove ou unlink - apaga o arquivo
os.rename - troca o nome ou move o arquivo
Vamos falar mais sobre o módulo json, mas:
json. dump = Gera um arquivo json
json.load
"""

caminho_arquivo = 'C:\\Users\\carol\\OneDrive\\Área de Trabalho\\Estudos-Python\\modulo-2\\Nova pasta Atenção\\'
caminho_arquivo += 'aula118.txt'

# with open(caminho_arquivo, 'w+') as arquivo: #W+ é escrita com possibilidade de leitura
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     arquivo.seek(0, 0)
#     print(arquivo.read)
#     print('Lendo')
#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip()) #strip tira os espaços, end tira o espaço só do fim
#     print(arquivo.readline().strip())
#     print('Readlines')
#     for linha in arquivo.readlines():
#         print(linha.strip())

# print('#' * 10)

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())
# arquivo = open(caminho_arquivo, 'r') 
#sempre fechar arquivos

#w abre o arquivo, apaga tudo q ta nele e escreve oq eu mandar

with open(caminho_arquivo, 'a') as arquivo: #W+ é escrita com possibilidade de leitura
    ...

#o a acrescenta, ao inves de apagar como o w 