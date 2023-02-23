import requests

#http: -> 80    roda automatico
#https:// -> 443
url = 'http://localhost:8000/'
response = requests.get(url)

print(response.status_code)
# print(response.headers)
#print(response.content) #conteúdo inteiro bagunçado
print(response.text) #html organizado
#print(response.json()) #erro pq a resposta n é em json