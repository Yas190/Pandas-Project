# %%
import pandas as pd
# %%
url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
# %%
# Ler tabelas diretamente de páginas html para um dataframe
df = pd.read_html(url)
df
# %%
# A funçao pegou todas as tabelas da pagina
len(df)
# %%
type(df)
# %%
# Selecionando a tabela de interesse
df_uf = df[1]
df_uf