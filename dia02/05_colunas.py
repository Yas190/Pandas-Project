# %%
import pandas as pd
# %%
df_transacoes = pd.read_csv("../data/transacoes.csv")
df_transacoes
# %%
df_transacoes.columns
# %%
df_transacoes.shape
# %%
df_transacoes.dtypes
# %%
# Renomear coluna
df_transacoes = df_transacoes.rename(columns={"qtdePontos": "qtPontos", 
                                              "descSistemaOrigem": "SistemaOrigem"})
# %%
# Selecionar colunas
df_transacoes[["idCliente", "qtPontos"]]