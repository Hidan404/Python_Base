from functools import reduce
from pathlib import Path


from pathlib import Path

def abrir_arquivo_passar_lista():
    caminho = Path(__file__).parent.resolve() / "emprestimos.csv"
    emprestimos = []
    
    with open(caminho, "r", encoding="utf-8") as f:
        linhas = f.readlines()[1:]  # pula o cabeçalho
        
    for linha in linhas:
        elementos = linha.strip().split(",")
        # Cria um dicionário com as chaves correspondentes
        dicionario = {
            'id_vendedor': elementos[0],                     # string ou pode converter para int
            'valor_emprestimos': float(elementos[1]),        # float
            'quantidade_emprestimos': int(elementos[2]),     # int
            'data': elementos[3]                             # string (ou int, se preferir)
        }
        emprestimos.append(dicionario)
    
    return emprestimos  




valor_emprerstimos = abrir_arquivo_passar_lista()
retorna_valor_emprestimos = map(lambda emp: float(emp["valor_emprestimos"]), valor_emprerstimos)
print(list(retorna_valor_emprestimos))

valor_emprestimos_lista_filtrada = filter(lambda positivo: positivo > 0, retorna_valor_emprestimos)
print(list(valor_emprestimos_lista_filtrada))