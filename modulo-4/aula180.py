# secrets gera números aleatórios seguros
import secrets
import string as s
from secrets import SystemRandom as sr

print(''.join (sr().choices(s.ascii_letters + s.digits + s.punctuation, k=10))) 
#gera uma senha aleatoria

random = secrets.SystemRandom()

#print(secrets.randbelow(100))

# random tem geradores de números pseudoaleatórios
# Obs.: números pseudoaleatórios significa que os números
# parecem ser aleatórios, mas na verdade não são. Portanto,
# este módulo não deve ser usado para segurança ou uso criptográfico.
# O motivo disso é que quando temos uma mesma entrada e um mesmo algorítimo,
# a saída pode ser previsível.
# doc: https://docs.python.org/pt-br/3/library/random.html
import random

# Funções:
# seed          NÃO FAZ nada
#   -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
#random.seed(0)

# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
# r_range = random.randrange(10, 20, 2) #pega de 10 a 20 pulando de 2 em 2
# print(r_range)

# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
# r_int = random.randint(10, 20)
# print(r_int)

# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
# r_uniform = random.uniform(10, 20) 
# print(r_uniform)

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
nomes = ['Luiz', 'Maria', 'Helena', 'Joana']
random.shuffle(nomes)
print(nomes)

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
# novos_nomes = random.sample(nomes, k=3) #k é o tamanho do sample, pega 2 
# #elementos aleatório de 2 itens da lista e armazena na variável
# print(nomes)
# print(novos_nomes)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
novos_nomes = random.choices(nomes, k=3)  #repete valores
print(nomes)
print(novos_nomes)

# random.choice(Iterável) -> Escolhe um elemento do iterável
print(random.choice(nomes))