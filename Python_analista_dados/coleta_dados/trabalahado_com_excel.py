import openpyxl
from pathlib import Path

caminho = Path(__file__).parent.resolve() / "banco.xlsx"
planilha = openpyxl.load_workbook(caminho)
planilha = planilha.active

saldo = []
cabecalho = next(planilha.values)
indice_saldo = cabecalho.index("balance")

saldo = [linha[indice_saldo] for linha in planilha.values if linha[indice_saldo] != "balance"]
print(saldo)