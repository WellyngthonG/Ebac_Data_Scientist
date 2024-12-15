import requests
from bs4 import BeautifulSoup

url = 'https://peps.python.org/'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text,'html.parser')

# Exibir o texto
#print(extracao.text.strip())

# Filtrar a exibição pela tag
for linha_texto in extracao.find_all('h2'):
    Título = linha_texto.text.strip()
    print('Título: ', Título)

'''
Desafio
Filtrar tags ['h2','p']
Contar quantos h2 e p existem no documento (linha_texto.name == tag)
'''

# Contar qtd de títulos e parágrafos
contar_titulos = 0
contar_paragrafos = 0

for linha_texto in extracao.find_all(['h2','p']):
    if linha_texto.name == 'h2':
        contar_titulos += 1 #Contar Títulos + 1
    elif linha_texto.name == 'p':
        contar_paragrafos += 1

print('Total de títulos', contar_titulos)
print('Total de parágrafos', contar_paragrafos)
#
# Exibir somente o texto das tags h2 e p
for linha_texto in extracao.find_all(['h2','p']):
    if linha_texto.name == 'h2':
        titulo = linha_texto.text.strip()
        print('Título: \n', titulo)
    elif linha_texto.name == 'p':
        paragrafo = linha_texto.text.strip()
        print('Parágrafo: \n', paragrafo)

# Exibir tags alinhadas
for titulo in extracao.find_all('h2'):
    print('\n Título:', titulo.text.strip())
    for link in titulo.find_next_siblings('p'):
        for a in link.find_all('a', href=True):
            print('Texto link: ', a.text.strip())

