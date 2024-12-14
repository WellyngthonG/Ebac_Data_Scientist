#Vamos continuar a partir dos dados gerados no exercício anterior.
#1 - Trate os campos ‘Marca’; ‘Material’ e ‘Temporada’ para os valores serem em minúsculo
#2 - Mantenha apenas os registros que tenham no mínimo 8 valores não nulos

import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('/data/ecommerce_ex2.csv')

# 1. Converter os campos 'Marca', 'Material' e 'Temporada' para letras minúsculas
df['Marca'] = df['Marca'].str.lower()  # Converte os valores para minúsculas
df['Material'] = df['Material'].str.lower()
df['Temporada'] = df['Temporada'].str.lower()

# Confirmando a conversão
print('Dados após conversão para minúsculas:\n', df[['Marca', 'Material', 'Temporada']].head())

# 2. Remover linhas com menos de 8 valores não nulos
df = df.dropna(thresh=8)  # Mantém apenas as linhas com pelo menos 8 valores não nulos

# Confirmando o resultado
print('DataFrame após remoção de linhas com menos de 8 valores não nulos:\n', df)
