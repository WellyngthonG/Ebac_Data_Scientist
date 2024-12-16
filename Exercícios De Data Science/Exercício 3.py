#Dando continuação ao exercício, vamos filtrar os produtos com maiores quantidades de comentários (N_Avaliações). Para isso, utilizaremos o método do Intervalo Interquartil (IQR).
#Passos:
#Calcular o IQR: O IQR é a diferença entre o terceiro quartil (Q3) e o primeiro quartil (Q1): iqr = q3 - q1.
#Determinar o Limite Superior para Outliers: O limite superior é calculado como limite_alto = q3 + 1.5 * iqr.
#Filtrar Produtos Acima do Limite: Filtre os produtos que têm N_Avaliações maior que limite_alto e armazene o resultado na variável df_avaliados.

import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('/data/ecommerce_ex3.csv')

# 1. Verificar os nomes das colunas
print('Nomes das colunas no DataFrame:', df.columns)

# 2. Calcular o intervalo interquartil (IQR) para a coluna de avaliações
coluna_avaliacoes = 'N_Avaliacoes'  # Usando o nome correto da coluna

q1 = df[coluna_avaliacoes].quantile(0.25)  # Primeiro quartil (Q1)
q3 = df[coluna_avaliacoes].quantile(0.75)  # Terceiro quartil (Q3)
iqr = q3 - q1  # Intervalo Interquartil (IQR)

# 3. Definir o limite superior para identificar outliers
limite_alto = q3 + 1.5 * iqr

# 4. Filtrar os produtos com N_Avaliacoes maior que o limite superior
df_avaliados = df[df[coluna_avaliacoes] > limite_alto]

# Exibir os resultados
print('Produtos com mais avaliações (outliers):\n', df_avaliados)
