# python netflix_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/netflix_titles.csv")
'''
# Visualizar as primeiras linhas
print("== primeiras 5 linhas ==")
print(df.head())

#Informações gerais
print("\n== info do DataFrame ==")
df.info()

#Verificar valores nulos
print("\n== valores nulos por coluna ==")
print(df.isnull().sum())
'''

'''
#Análises adicionais para o projeto
#   a) Distribuição por tipo (Movie vs TV Show)

counts = df['type'].value_counts()
sns.barplot(x=counts.index, y=counts.values, palette="viridis")
plt.title("Distribuição: Filmes vs Séries")
plt.savefig("../outputs/figures/type_distribution.png")
plt.close()

#   b) Evolução de lançamentos por ano
year_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(12,5))
sns.lineplot(x=year_counts.index, y=year_counts.values)
plt.title("Lançamentos por ano")
plt.xlabel("Ano")
plt.ylabel("Quantidade")
plt.savefig("../outputs/figures/releases_per_year.png")
plt.close()

#   c) Top 10 países com mais títulos
top_countries = df['country'].value_counts().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index, palette="magma")
plt.title("Top 10 países com mais títulos")
plt.savefig("../outputs/figures/top_countries.png")
plt.close()


#   d) Gêneros mais frequentes
#      A coluna listed_in contém gêneros separados por vírgula.
#      Transforme em formato “explodido”:

# separar os gêneros
genres = df['listed_in'].dropna().str.split(', ')
all_genres = [genre for sublist in genres for genre in sublist]
genres_series = pd.Series(all_genres)

top_genres = genres_series.value_counts().head(10)
sns.barplot(x=top_genres.values, y=top_genres.index, palette="cubehelix")
plt.title("Top 10 gêneros mais comuns")
plt.savefig("../outputs/figures/top_genres.png")
plt.close()

#   e) Tempo médio de duração (filmes)
movies = df[df['type']=="Movie"].copy()

def duration_to_minutes(x):
    try:
        return int(x.replace(" min",""))
    except:
        return None

movies['duration_min'] = movies['duration'].apply(duration_to_minutes)

print("Duração média dos filmes:", movies['duration_min'].mean())
'''

#4) Exportar resultados
# Salva tabelas auxiliares (para mostrar que sabe exportar):
top_genres.to_csv("../outputs/tables/top_genres.csv")
top_countries.to_csv("../outputs/tables/top_countries.csv")
