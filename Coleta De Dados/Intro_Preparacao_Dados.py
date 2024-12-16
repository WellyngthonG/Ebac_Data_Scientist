# Análise exploratória de dados (AED)
import pandas as pd


df = pd.read_csv('C:/Users/welly/PycharmProjects/ColetaDados/clientes-v2.csv')

print(df.head().to_string())
print(df.tail().to_string())
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

print('Verificação inicial:')
print(df.info())

print('Análise de dados nulos:\n', df.isnull().sum())
print('% de dados nulos:\n', df.isnull().mean() * 100)
df.dropna(inplace=True)
print('Confirmar remoção de dados nulos:', df.isnull().sum().sum())

print('Análise de dados duplicados:\n', df.duplicated().sum())

print('Análise de dados únicos:\n', df.nunique())

print('Estatísticas de dados:\n', df.describe())

df = df[['idade', 'data', 'estado','salario', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao']]
print(df.head().to_string())

df.to_csv('clientes-v2-tratados.csv', index=False)
