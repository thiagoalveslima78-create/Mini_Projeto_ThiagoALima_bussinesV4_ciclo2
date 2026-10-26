
#%%
#===========================================================================
# Importação de bibliotecas, importação de dados, validação do tipo de dados
#===========================================================================
import kagglehub
import csv
import pandas as pd
from datetime import datetime

#importar o arquivo do Kaggle
path = kagglehub.dataset_download("namespaiva/base-varejo")
print("Path to dataset files:", path)

#criação do data frama
df = pd.read_csv('Base Varejo.csv', sep=';')

#verificar os tipos de dados das series
print(df.head)
print(df.shape)
print(df.dtypes)

#%%
#===========================================================================
# SPRINT 2 - VALIDAÇÃO DE CELULAS VAZIAS, CONVERSÃO DE DADOS
#===========================================================================
import pandas as pd
import csv

df = pd.read_csv('Base Varejo.csv', sep=';')

df_DATA = pd.to_datetime(df['DATA'], format="%d/%m/%Y", errors='coerce')
print(df_DATA.dtypes)
print(df_DATA)


#verificar linhas vazias, nas seções
dfnulo = df.isna().sum()
print(dfnulo)


# #Abrir o arquivo e formatar os dados 
# with open('Base Varejo.csv', newline='') as arq:
#     leitor = csv.DictReader(arq, delimiter =";")
#     for linha in leitor:
#         print(linha)
        
# %%
#===========================================================================
# SPRINT 3 - LIMPEZA DE NULOS E DUPLICATAS
#===========================================================================
import pandas as pd

df = pd.read_csv('Base Varejo.csv', sep=';')

df_limpo = df.dropna(axis=1)
print(df_limpo)
# %%
#===========================================================================
# SPRINT 4 - ESTATISTICA DESCRITIVA
#===========================================================================
import pandas as pd
from collections import Counter

df = pd.read_csv('Base Varejo.csv', sep=';')

#limpeza das colunas adicionais, sem valores
df_limpo = df.dropna(axis=1)

#estatistica descritiva da coluna de filhos
print(df_limpo['CL_FHL'].describe())

#filtro das quantidades de registros por código de cliente
filtro = df['CL_ID'].value_counts().reset_index()
print(filtro)

# visão agrupadas da qtd de filhos por cliente
regitros_unicos_de_clintes =(pd.unique(df_limpo['CL_ID']))
print(regitros_unicos_de_clintes)

filtro = df.groupby('CL_ID')['CL_FHL'].mean()
print(filtro)

tabela_dinamica = df_limpo.pivot_table(
    index ='CL_GENERO',
    columns = 'CO_ID',
    aggfunc = 'size'
)
print(tabela_dinamica)