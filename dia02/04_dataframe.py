# %%
import pandas as pd
# %%
df_clientes = pd.read_csv("../data/clientes.csv")
df_clientes
# %%
# Topo do dataframe
df_clientes.head(n=10)
# %%
# Bottom do dataframe
df_clientes.tail(n=10)
# %%
# Amostra aleatoria
df_clientes.sample(n = 10)
# %%
# Numero de linhas e colunas do dataframe
df_clientes.shape
# %%
# Colunas do dataframe
df_clientes.columns
# %%
df_clientes.index
# %%
# Informacoes gerais do dataframe
df_clientes.info()
# %%
# Tipos das colunas
df_clientes.dtypes
# %%
