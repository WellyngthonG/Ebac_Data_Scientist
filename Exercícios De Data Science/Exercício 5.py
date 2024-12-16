#Preparação de dados 1
#Vamos continuar o nosso projeto, realizando agora a preparação dos dados. Seu código deve conter os passos a seguir:

#Verifique a quantidade de dados únicos para cada campo e armazene na variável unicos.
#Verifique as estatísticas dos campos numéricos e armazene na variável estatisticas.
#Crie o campo Preco com esse cálculo em relação aos campos: Reais + (Centavos/100). O novo campo deve ser criado no mesmo DataFrame df.
#Remova os seguintes campos: ['Reais', 'Centavos', 'Condicao', 'Condicao_Atual']. A remoção deve ser feita no mesmo DataFrame df.

import pandas as pd

# Carregar os dados
df = pd.read_csv('/data/ecommerce_tratados.csv')

# Verifica a quantidade de dados únicos em cada coluna
unicos = df.nunique()
print('Análise de dados únicos:\n', unicos)

# Calcula estatísticas descritivas dos campos numéricos
estatisticas = df.describe()
print('Estatísticas dos dados:\n', estatisticas)

# Cria o campo "Preco" com o cálculo em relação aos campos "Reais" e "Centavos"
df['Preco'] = df['Reais'] + (df['Centavos'] / 100)

# Remove os campos especificados
df = df.drop(columns=['Reais', 'Centavos', 'Condicao', 'Condicao_Atual'])

# Mostra a estrutura do DataFrame atualizado
print('DataFrame após alterações:\n', df.head())
