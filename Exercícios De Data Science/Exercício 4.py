#Finalize o exercício seguindo os passos abaixo:
#Converta a coluna Desconto para o tipo string.
#Modifique a coluna Desconto para exibir apenas o valor numérico do desconto (por exemplo, "18% OFF" deve se tornar "18").
#Crie duas novas colunas baseadas na coluna Condicao:
#Condicao_Atual: Extraia a primeira parte do campo Condicao (por exemplo, "Novo | +10mil vendidos" deve se tornar "Novo").
#Qtd_Vendidos: Extraia a quantidade de itens vendidos do campo Condicao (por exemplo, "Novo | +10mil vendidos" deve se tornar "+10mil"). Se não houver quantidade especificada, escreva "Nenhum".

import pandas as pd

df = pd.read_csv('/data/ecommerce_ex4.csv', encoding='utf-8')

# Escreva seu código abaixo

# Extrair e limpar os dados da coluna 'Condicao'
# A função lambda é usada aqui para pegar a primeira palavra da string na coluna 'Condicao'
# x.split(' ')[0] pega a primeira palavra da string.
df['Condicao_Atual'] = df['Condicao'].apply(lambda x: x.split(' ')[0].strip())

# A função lambda é usada aqui para pegar a quinta palavra da string na coluna 'Condicao' se existir,
# caso contrário, retorna 'Nenhum'
df['Qtd_Vendidos'] = df['Condicao'].apply(lambda x: x.split(' ')[4].strip() if len(x.split(' ')) > 1 else 'Nenhum')


# Converter a coluna 'Desconto' para string
df['Desconto'] = df['Desconto'].astype(str)

# A função lambda é usada aqui para remover o símbolo '%' da string na coluna 'Desconto'
df['Desconto'] = df['Desconto'].apply(lambda x: x.split('%')[0].strip())
