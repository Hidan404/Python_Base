from pathlib import Path
import pandas as pd



caminho_arquivo = Path(__file__).parent / "dados_sujos.csv"


def visualizar_dados():
    df = pd.read_csv(caminho_arquivo)
    print(df.head())
    print(df.info())
    print(df.describe())
    print(df.columns)

visualizar_dados()    


def tratar_dados():
    df = pd.read_csv(caminho_arquivo)
    df.drop_duplicates(subset=["id"], inplace=True)
    df["departamento"] = df["departamento"].str.strip()
    #print(df["departamento"])

    return df

df_limpo = tratar_dados()


ids = df_limpo.loc[0:, "id"].to_list()
ids.sort()

df = pd.read_csv(caminho_arquivo)
print(df[["id","salario"]].describe().T)
print(df[["nome", "departamento"]].describe().T)
nomes = df.loc[0:, "nome"]
print(type(nomes))
print(nomes[lambda nome: nome.str.startswith("A")])