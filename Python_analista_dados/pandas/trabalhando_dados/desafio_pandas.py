'''
1 carregar arquivo.csv com feedback de clientes
2 usar um llm para classificar o sentimento de cada feedback
(Positivo, Negativo, Neutro)
3 adicionar uma nova coluna com essa classificação do dataframe
'''
import pandas as pd
from pathlib import Path
from google import genai
import os
from dotenv import load_dotenv
import pandas as pd


load_dotenv()



def carregar_arquivo():
    caminho = Path(__file__).parent.resolve() / "reviews_fixed.csv"
    with open(caminho, "r", encoding="utf-8") as arquivo:
        
        df = pd.DataFrame(arquivo)

    return df    

df = carregar_arquivo()

df = pd.read_csv(
    Path(__file__).parent.resolve() / "reviews_fixed.csv",
    sep=",",
    quotechar='"',
    engine='python',
    on_bad_lines='skip',   # ignora linhas muito problemáticas
    encoding='utf-8'
)
print(df.head())
print(df.shape)
print(df["reviewerName"])

def classificar_sentimento():
    modelo = "gemini-3.1-flash-lite"
    cliente = genai.Client(api_key=os.getenv("CHAVE_APY"))


