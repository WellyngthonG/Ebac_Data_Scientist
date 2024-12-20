import pandas as pd
from sklearn.preprocessing import (RobustScaler, MinMaxScaler ,StandardScaler)

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('clientes-v2-tratados.csv')

print(df.head())

df = df.drop(['data', 'estado', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao'], axis=1)
# Ou poderia somente colocar df = df[['idade', 'salario']]

# Normalização - MinMaxScaler.
scaler = MinMaxScaler()
df['idadeMinMaxScaler'] = scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler'] = scaler.fit_transform(df[['salario']])

min_max_scaler = MinMaxScaler(feature_range=(-1,1))
df['idadeMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['salario']])

# Padronização StandardScaler
scaler = RobustScaler()
df['idadeStandardScaler'] = scaler.fit_transform(df[['idade']])
df['salarioStandardScaler'] = scaler.fit_transform(df[['salario']])

# Padronização RobustScaler
scaler = RobustScaler()
df['idadeRobustScaler'] = scaler.fit_transform(df[['idade']])
df['salarioRobustScaler'] = scaler.fit_transform(df[['salario']])

print(df.head(15))

print('MinMaxScaler (De 0 a 1):')
print('Idade - Min: {:.4f} Max: {:4f} Mean: {:.4f} Std: {:.4f}'.format(df['idadeMinMaxScaler'].min(), df['idadeMinMaxScaler'].max(), df['idadeMinMaxScaler'].mean(), df['idadeMinMaxScaler'].std()))
print('Salário - Min: {:.4f} Max: {:4f} Mean: {:.4f} Std: {:.4f}'.format(df['salarioMinMaxScaler'].min(), df['salarioMinMaxScaler'].max(), df['salarioMinMaxScaler'].mean(), df['salarioMinMaxScaler'].std()))

print('\nMinMaxScaler (De -1 a 1):')
print('Idade - Min: {:.4f} Max: {:4f} Mean: {:.4f} Std: {:.4f}'.format(df['idadeMinMaxScaler'].min(), df['idadeMinMaxScaler'].max(), df['idadeMinMaxScaler'].mean(), df['idadeMinMaxScaler'].std()))
print('Salário - Min: {:.4f} Max: {:4f} Mean: {:.4f} Std: {:.4f}'.format(df['salarioMinMaxScaler'].min(), df['salarioMinMaxScaler'].max(), df['salarioMinMaxScaler'].mean(), df['salarioMinMaxScaler'].std()))

print('\nStandardScaler (Ajuste a média a 0 e desvio de padrão a 1):')
print('Idade - Min: {:.4f} Max: {:4f} Mean: {:.18f} Std: {:.4f}'.format(df['idadeMinMaxScaler'].min(), df['idadeMinMaxScaler'].max(), df['idadeMinMaxScaler'].mean(), df['idadeMinMaxScaler'].std()))
print('Salário - Min: {:.4f} Max: {:4f} Mean: {:.18f} Std: {:.4f}'.format(df['salarioMinMaxScaler'].min(), df['salarioMinMaxScaler'].max(), df['salarioMinMaxScaler'].mean(), df['salarioMinMaxScaler'].std()))

print('\nRobustScaler (Ajuste a mediana e IQR):')
print('Idade - Min: {:.4f} Max: {:4f} Mean: {:.4f} Std: {:.4f}'.format(df['idadeMinMaxScaler'].min(), df['idadeMinMaxScaler'].max(), df['idadeMinMaxScaler'].mean(), df['idadeMinMaxScaler'].std()))
print('Salário - Min: {:.4f} Max: {:4f} Mean: {:.4f} Std: {:.4f}'.format(df['salarioMinMaxScaler'].min(), df['salarioMinMaxScaler'].max(), df['salarioMinMaxScaler'].mean(), df['salarioMinMaxScaler'].std()))

