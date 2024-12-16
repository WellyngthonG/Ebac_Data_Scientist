# Preparação de dados 3
# Vamos finalizar o exercício com mais algumas preparações. Siga os passos a seguir. Todos campos devem ser criado no mesmo DataFrame df:
#
# Crie o campo Qtd_Vendidos_Cod com a transformação do campo Qtd_Vendidos para número de acordo com as suas grandezas ('Nenhum', '1', '2', '3', '4', '+5', '+25', '+50', '+100', '+1000', '+10mil' '+50mil'), exemplo +10mil = 10000.
# Crie o campo Marca_Freq com a transformação do campo Marca para número de acordo com a frequência do valor.
# Crie o campo Material_Freq com a transformação do campo Material para número de acordo com a frequência do valor.

import pandas as pd

# Carregar o DataFrame
df = pd.read_csv('/data/ecommerce_tratados_ex3.csv')

# Dicionário para converter as grandezas do campo Qtd_Vendidos em números
qtd_vendidos_mapping = {
    'Nenhum': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '+5': 5,
    '+25': 25,
    '+50': 50,
    '+100': 100,
    '+1000': 1000,
    '+10mil': 10000,
    '+50mil': 50000
}

# Criar o campo Qtd_Vendidos_Cod com base no mapeamento
df['Qtd_Vendidos_Cod'] = df['Qtd_Vendidos'].map(qtd_vendidos_mapping)

# Calcular a frequência relativa de cada marca (contagem normalizada)
marca_freq = df['Marca'].value_counts() / len(df)

# Criar o campo Marca_Freq com a frequência relativa
df['Marca_Freq'] = df['Marca'].map(marca_freq)

# Calcular a frequência relativa de cada material (contagem normalizada)
material_freq = df['Material'].value_counts() / len(df)

# Criar o campo Material_Freq com a frequência relativa
df['Material_Freq'] = df['Material'].map(material_freq)

# Exibir os primeiros registros para verificar as alterações
print(df.head())
