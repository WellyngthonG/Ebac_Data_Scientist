from urllib.request import Request

import requests
from bs4 import BeautifulSoup
import pandas as pd
# Altere para usar "pd" como convenção de importação

print('Request: ')
# Response é a variável, que está recebendo o requests. O .get é para buscar o que está entre o (" ")
response = requests.get('https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)')

# Print é para mostrar na tela o que está dentro da variável response.
# O .text é para mostrar o texto e o [:600] é para mostrar os primeiros 600 caracteres.
print(response.text[:600])

print('BeautifulSoup: ')
# Atributo é o que está dentro do () e é a característica daquele dado
soup = BeautifulSoup(response.text,'html.parser')
print(soup.prettify()[:1000])

print('Pandas: ')
url_dados = pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)')
print(url_dados[0].head(10))