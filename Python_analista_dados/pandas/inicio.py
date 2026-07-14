import pandas as pd

dados = {
    "id": [1, 2, 3],
    "data": ["2024-01-01", "2024-01-02", "2024-01-03"],
    "valor": [100, 150, 200],
    "categoria": ["A", "B", "A"],
}

transformar_dataframes = pd.DataFrame(dados)
print("\n",transformar_dataframes, "\n")

colunas = transformar_dataframes.columns
print(colunas)

print(transformar_dataframes.count())
print(transformar_dataframes.describe())

print(transformar_dataframes.shape)
print(transformar_dataframes.tail(n=1))
print(transformar_dataframes.info())