"""
Closure e funções que retornam outras funções
Ele precisa salvar os dados na memória para executar
"""

def criar_saudacao(saudacao, nome):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia', 'Luiz')
falar_boa_noite = criar_saudacao('Boa noite', 'Luiz')


for nome in ['Maria', 'Joana', 'Carol']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))