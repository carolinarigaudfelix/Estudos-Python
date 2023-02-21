#json.dump e json.load com arquivos ao invés de strings
import json
import os

NOME_ARQUIVO = 'aula173.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join( #une duas coisas, dirname e NOME_ARQUIVO
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)
print(os.path.join(
    os.path.dirname(__file__),
    NOME_ARQUIVO
))



filme = {
        'title': 'O Senhor dos Anéis: A Sociedade do Anel', 
        'original_title': 'The Lord of the Rings: The Fellowship of the Ring', 
        'is_movie': True, 
        'imdb_rating': 8.8, 
        'year': 2001, 
        'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'], 
        'budget': None
}

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as arquivo:
    json.dump(filme, arquivo)


with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo:
    filme_do_json = json.load(arquivo)
    print(filme_do_json)
