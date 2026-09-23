import os

# Cores ANSI para deixar o terminal mais agradável.
RESET = "\033[0m"
NEGRITO = "\033[1m"
CIANO = "\033[96m"
AZUL = "\033[94m"
VERDE = "\033[92m"
AMARELO = "\033[93m"
VERMELHO = "\033[91m"

def colorir(texto, cor):
    return f"{cor}{texto}{RESET}"

def titulo(texto):
    linha = "═" * 42
    print(colorir(f"\n╔{linha}╗", CIANO + NEGRITO))
    print(colorir(f"║{texto.center(42)}║", CIANO + NEGRITO))
    print(colorir(f"╚{linha}╝", CIANO + NEGRITO))

# Nome do arquivo onde o histórico será salvo
ARQUIVO_HISTORICO = "historico_gastos.txt"

def carregar_historico():
    """Exibe o histórico salvo se o arquivo existir."""
    if os.path.exists(ARQUIVO_HISTORICO):
        titulo("HISTÓRICO DE MESES ANTERIORES")
        with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as f:
            print(colorir(f.read(), AZUL))
        print(colorir("─" * 42, CIANO))
    else:
        print(colorir("\n⚠ Nenhum histórico antigo encontrado ainda.", AMARELO))

def salvar_no_arquivo(texto_mes):
    """Salva os dados do mês atual no arquivo de texto."""
    with open(ARQUIVO_HISTORICO, "a", encoding="utf-8") as f:
        f.write(texto_mes + "\n" + "="*40 + "\n")

def registrar_mes():
    titulo("NOVO LANÇAMENTO MENSAL")
    mes_ano = input("Digite o Mês e Ano (Ex: Janeiro/2027): ").strip()
    
    # Valores base pré-configurados
    salario_liquido = 2735.00
    meta_poupanca = 450.00
    
    # Dicionário com os seus gastos fixos estruturados
    gastos = {
        "Aluguel": 700.00,
        "Alimentação": 300.00,
        "Energia Elétrica (Luz)": 260.00,
        "Internet Fixa": 150.00,
        "Moto (Gasolina/Manutenção)": 130.00,
        "Reserva do Gás": 30.00
    }
    
    print(f"\nConfigurando base para {mes_ano}...")
    print(f"-> Salário Líquido considerado: R$ {salario_liquido:.2f}")
    print(f"-> Meta de Poupança considerada: R$ {meta_poupanca:.2f}")
    
    # Loop para adicionar gastos adicionais ou variáveis (Mangás, saídas, etc)
    while True:
        resposta = input("\nDeseja adicionar algum outro gasto ou variável para este mês? (s/n): ").lower().strip()
        if resposta != 's':
            break
        
        nome_gasto = input("Nome do gasto (Ex: Mangás, Cinema, Farmácia): ").strip()
        try:
            valor_gasto = float(input(f"Valor para '{nome_gasto}': R$ "))
            if nome_gasto in gastos:
                gastos[nome_gasto] += valor_gasto
            else:
                gastos[nome_gasto] = valor_gasto
        except ValueError:
            print(colorir("Valor inválido! Digite apenas números separados por ponto (Ex: 35.90).", VERMELHO))

    # Cálculos
    total_gastos = sum(gastos.values())
    saldo_final_lazer = salario_liquido - meta_poupanca - total_gastos
    
    # Montando a string formatada para exibição e salvamento
    saida = f"\nMÊS/ANO: {mes_ano}\n"
    saida += f"Salário Líquido: R$ {salario_liquido:.2f}\n"
    saida += f"Dinheiro Separado (Poupança): R$ {meta_poupanca:.2f}\n"
    saida += "--- Detalhamento dos Gastos ---\n"
    for item, valor in gastos.items():
        saida += f"  - {item}: R$ {valor:.2f}\n"
    saida += f"Total de Gastos: R$ {total_gastos:.2f}\n"
    saida += f"SALDO LIVRE RESTANTE: R$ {saldo_final_lazer:.2f}\n"
    
    # Exibe na tela o resumo
    titulo("RESUMO DO MÊS CALCULADO")
    print(colorir(saida, VERDE))
    
    # Salva os dados permanentemente
    salvar_no_arquivo(saida)
    print(colorir(f"✓ Os dados de {mes_ano} foram salvos em '{ARQUIVO_HISTORICO}'!", VERDE))

def menu():
    while True:
        titulo("GERENCIADOR FINANCEIRO")
        print(colorir("  1. 📚 Ver Histórico de Gastos Salvos", AZUL))
        print(colorir("  2. 💰 Lançar Novo Mês", VERDE))
        print(colorir("  3. 🚪 Sair", AMARELO))
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            carregar_historico()
        elif opcao == "2":
            registrar_mes()
        elif opcao == "3":
            print(colorir("\nFechando o programa. Até o próximo mês! 👋", CIANO))
            break
        else:
            print(colorir("\nOpção inválida! Escolha 1, 2 ou 3.", VERMELHO))

if __name__ == "__main__":
    menu()
