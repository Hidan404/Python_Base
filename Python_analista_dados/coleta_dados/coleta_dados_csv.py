import csv
from pathlib import Path
import statistics

dados = [
    ["age", "job", "marital", "education", "default", "balance", "housing", "loan"],
    [45, "admin.", "married", "secondary", "no", 1200, "yes", "no"],
    [32, "technician", "single", "tertiary", "no", 230, "no", "yes"],
    [58, "management", "married", "tertiary", "no", 3500, "yes", "no"],
    [28, "services", "single", "secondary", "no", -150, "yes", "yes"],
    [41, "blue-collar", "divorced", "primary", "no", 850, "no", "no"],
    [50, "retired", "married", "secondary", "no", 600, "yes", "no"],
    [36, "entrepreneur", "married", "tertiary", "yes", 1500, "yes", "yes"],
    [24, "student", "single", "tertiary", "no", 100, "no", "no"],
    [62, "retired", "married", "primary", "no", 4200, "yes", "no"],
    [33, "technician", "married", "secondary", "no", 500, "no", "yes"],
    [47, "management", "divorced", "tertiary", "no", 2100, "yes", "no"],
    [29, "services", "single", "secondary", "no", -200, "no", "no"],
    [55, "admin.", "married", "secondary", "no", 1800, "yes", "yes"],
    [38, "self-employed", "married", "tertiary", "no", 950, "yes", "no"],
    [31, "blue-collar", "single", "primary", "no", 300, "no", "no"],
    [43, "technician", "divorced", "secondary", "no", 1100, "yes", "yes"],
    [26, "student", "single", "tertiary", "no", 50, "no", "no"],
    [59, "management", "married", "tertiary", "no", 2800, "yes", "no"],
    [35, "services", "single", "secondary", "yes", 400, "yes", "yes"],
    [48, "admin.", "married", "tertiary", "no", 1300, "no", "no"],
    [53, "retired", "divorced", "primary", "no", 550, "yes", "no"],
    [27, "technician", "single", "secondary", "no", 680, "no", "yes"],
    [40, "entrepreneur", "married", "tertiary", "no", 2500, "yes", "no"],
    [34, "blue-collar", "married", "secondary", "no", 720, "yes", "yes"],
    [46, "self-employed", "single", "tertiary", "no", 1600, "no", "no"],
]

def criar_csv(dado):
    caminho_csv = Path(__file__).parent.resolve() / "banco.csv"
    with open(caminho_csv, "w", newline="", encoding="utf-8") as arquivo:
        arquivo_gerar = csv.writer(arquivo)
        arquivo_gerar.writerows(dado)

def extrair_age():
    caminho_csv = Path(__file__).parent.resolve() / "banco.csv"
    with open(caminho_csv, "r") as f:
        dados = f.readlines()[1:]
        idades = [int(age.split(",")[0]) for age in dados]
        print(idades)

def extrair_balance(dado):
    caminho_csv = Path(__file__).parent.resolve() / "banco.csv"
    with open(caminho_csv, "r", encoding="utf-8") as arquivo:  
        leior_iter = csv.reader(arquivo, delimiter=",")
        cabecalho = next(leior_iter)
        balance_indice = cabecalho.index("balance")
        saldo = [int(bal[balance_indice]) for bal in leior_iter]

    saldo_positivo = list(map(lambda valor: valor  if valor > 0 else None, saldo))
    saldo_positivo_limpo = [valor for valor in saldo_positivo if valor is not None]
    media_idade = statistics.mean(saldo)
    mediana_idade = statistics.median(saldo)
    print(saldo)
    print(saldo_positivo_limpo)
    print(media_idade)
    print(mediana_idade)    

extrair_balance(dados)


