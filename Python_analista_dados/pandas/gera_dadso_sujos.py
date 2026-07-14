import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Semente para reproducibilidade
random.seed(42)
np.random.seed(42)

# Lista de nomes (com alguns erros propositais)
nomes = [
    "Ana Silva", "João Pereira", "Maria Oliveira", "Carlos Souza", "Fernanda Lima",
    "Ricardo Alves", "Juliana Costa", "Paulo Santos", "Camila Rocha", "Lucas Mendes",
    "Bruna Ferreira", "Rafael Barbosa", "Amanda Gomes", "Diego Martins", "Larissa Castro",
    "Felipe Azevedo", "Tatiana Cardoso", "Marcelo Ribeiro", "Patricia Nunes", "Rodrigo Barros"
]
departamentos = ["Vendas", "Marketing", "RH", "Financeiro", "TI", "Operações", "Logística"]

def gera_data():
    """Gera data com formatos variados e algumas inválidas"""
    ano = random.randint(2018, 2025)
    mes = random.randint(1, 12)
    dia = random.randint(1, 28)
    data = datetime(ano, mes, dia)
    formato = random.choice(['%Y-%m-%d', '%d/%m/%Y', '%m-%d-%Y'])
    if random.random() < 0.05:  # 5% de datas inválidas
        return "31/02/2023"  # Data inválida
    return data.strftime(formato)

# Gerar 100 linhas
dados = []
ids = list(range(1, 101))
random.shuffle(ids)  # Embaralha para criar IDs fora de ordem

for i in range(100):
    id_ = ids[i]
    nome = random.choice(nomes)
    # Introduz erros de digitação em alguns nomes
    if random.random() < 0.1:
        nome = nome.replace('ã', 'a').replace('ç', 'c').replace('é', 'e')
    idade = random.randint(22, 60)
    if random.random() < 0.08:
        idade = random.choice([150, -5, np.nan])  # outliers e NaN
    salario = round(random.uniform(3000, 12000), 2)
    if random.random() < 0.07:
        salario = random.choice([np.nan, -1000, 1000000])
    data_adm = gera_data()
    dep = random.choice(departamentos)
    if random.random() < 0.06:
        dep = dep + " "  # espaço extra
    projetos = random.randint(0, 15)
    if random.random() < 0.08:
        projetos = random.choice([-3, np.nan])
    avaliacao = round(random.uniform(0, 10), 1)
    if random.random() < 0.07:
        avaliacao = random.choice([np.nan, 20.0, -2.0])
    # Bonus com múltiplos formatos
    bonus_opcoes = ["Sim", "Não", "TRUE", "FALSE", "1", "0", np.nan]
    bonus = random.choice(bonus_opcoes)
    if random.random() < 0.05:
        bonus = "Talvez"  # inválido
    obs = random.choice(["", "Funcionário destaque", "Precisa de treinamento", "Observação com çãé", None])
    # Duplicar algumas linhas
    if random.random() < 0.07 and i > 0:
        # copia a linha anterior, mudando observação
        dados.append(dados[-1].copy())
        dados[-1]["observacoes"] = "DUPLICADA"
    else:
        dados.append({
            "id": id_,
            "nome": nome,
            "idade": idade,
            "salario": salario,
            "data_admissao": data_adm,
            "departamento": dep,
            "projetos": projetos,
            "avaliacao": avaliacao,
            "bonus": bonus,
            "observacoes": obs
        })

# Garantir exatamente 100 linhas (cortar ou preencher)
if len(dados) > 100:
    dados = dados[:100]
elif len(dados) < 100:
    while len(dados) < 100:
        dados.append(dados[-1].copy())

df = pd.DataFrame(dados)
df.to_csv("dados_sujos.csv", index=False, encoding="utf-8-sig")
print("Arquivo 'dados_sujos.csv' gerado com sucesso!")