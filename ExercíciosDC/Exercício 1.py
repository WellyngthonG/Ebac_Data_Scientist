#Vamos continuar o nosso projeto, realizando o tratamento de dados. Para facilitar, algumas questões, especifiquei os nomes dos campos, pois iremos usar em outros exercícios. Passo a passo:
#1 - Verifique a quantidade de linhas e colunas e armazene na variável linhas_colunas.
#2 - Verifique os tipos de dados de todo o dataframe e armazene na variável tipos.
#3 - Verifique a quantidade de valores nulos e armazene na variável nulos.
#4 - Substitua, no mesmo dataframe, os valores nulos das colunas ‘Temporada’ e ‘Marca’ por ‘Não Definido’.

import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('/data/ecommerce.csv')

# 1. Obter a quantidade de linhas e colunas
linhas_colunas = df.shape  # Retorna uma tupla (n_linhas, n_colunas)
print('Verificar a qtd de Linhas e Colunas: ', linhas_colunas)

# 2. Obter os tipos de dados de cada coluna
tipos = df.dtypes  # Retorna uma série com os tipos de dados
print('Verificar Tipagem:\n', tipos)

# 3. Calcular a quantidade de valores nulos em cada coluna
nulos = df.isnull().sum()  # Retorna uma série com a soma de valores nulos por coluna
print('Verificar valores nulos:\n', nulos)

# 4. Substituir valores nulos das colunas 'Temporada' e 'Marca' por 'Não Definido'
df['Temporada'] = df['Temporada'].fillna('Não Definido')  # Atualiza a coluna com valores substituídos
df['Marca'] = df['Marca'].fillna('Não Definido')          # Atualiza a coluna com valores substituídos

# Confirmando a substituição dos valores nulos
nulos_atualizados = df.isnull().sum()  # Verifica novamente os valores nulos
print('Valores nulos após substituição:\n', nulos_atualizados)
