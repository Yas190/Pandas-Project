# %%
import pandas as pd
# %%
# Importando dados de csv. Se for necessario especificar o
# separador, usar "sep = "
df = pd.read_csv("../data/clientes.csv")
df
# %%
# Salvando os dados como csv. Por padrao, cria uma coluna
# de index que pode ser removida com "index = False"
df.to_csv("clientes.csv")
# %%
# Salvando os dados como parquet
df.to_parquet("clientes.parquet", index = False)
# %%
df_2 = pd.read_parquet("clientes.parquet")
df_2
# %%
df.to_excel("clientes.xlsx")
# %%
df_3 = pd.read_excel("clientes.xlsx")
df_3
# %%
