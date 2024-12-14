#Finalize o exercício seguindo os passos abaixo:
#Converta a coluna Desconto para o tipo string.
#Modifique a coluna Desconto para exibir apenas o valor numérico do desconto (por exemplo, "18% OFF" deve se tornar "18").
#Crie duas novas colunas baseadas na coluna Condicao:
#Condicao_Atual: Extraia a primeira parte do campo Condicao (por exemplo, "Novo | +10mil vendidos" deve se tornar "Novo").
#Qtd_Vendidos: Extraia a quantidade de itens vendidos do campo Condicao (por exemplo, "Novo | +10mil vendidos" deve se tornar "+10mil"). Se não houver quantidade especificada, escreva "Nenhum".

import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('/data/ecommerce_ex4.csv', encoding='utf-8')

# 1. Extrair e limpar os dados da coluna 'Condicao'
# Criando a coluna 'Condicao_Atual' com a primeira palavra antes do '|'
df['Condicao_Atual'] = df['Condicao'].apply(lambda x: x.split(' |')[0])

# 2. Criando a coluna 'Qtd_Vendidos' com a quantidade de itens vendidos ou "Nenhum"
# Extraímos a parte que contém a quantidade de vendidos, após o '|', caso exista
df['Qtd_Vendidos'] = df['Condicao'].apply(lambda x: x.split(' |')[1].split(' ')[0] if 'vendidos' in x else 'Nenhum')

# 3. Converter a coluna 'Desconto' para string
df['Desconto'] = df['Desconto'].astype(str)

# 4. Modificar a coluna 'Desconto' para exibir apenas o valor numérico
df['Desconto'] = df['Desconto'].apply(lambda x: x.replace('%', '') if '%' in x else x)

# Exibir o DataFrame resultante
print(df[['Condicao_Atual', 'Qtd_Vendidos', 'Desconto']])
