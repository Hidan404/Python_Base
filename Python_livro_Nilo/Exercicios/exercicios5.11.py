def juros_poupanca():
    deposito_inicial = float(input("Depósito inicial: "))
    juros = 0.10
    saldo = deposito_inicial
    total_depositado = deposito_inicial

    for mes in range(1, 25):
        deposito_mensal = float(input(f"Digite depósito mensal {mes}: "))
        saldo += deposito_mensal
        total_depositado += deposito_mensal
        saldo += saldo * juros
        print(f"Saldo após o mês {mes}: R$ {saldo:.2f}")

    ganhos = saldo - total_depositado
    print(f"Depósito inicial: R$ {deposito_inicial:.2f}")
    print(f"Total depositado: R$ {total_depositado:.2f}")
    print(f"Ganhos em juros: R$ {ganhos:.2f}")
    print(f"Saldo final: R$ {saldo:.2f}")


juros_poupanca()