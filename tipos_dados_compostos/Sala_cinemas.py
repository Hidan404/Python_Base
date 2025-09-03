lugares_vagos = []
lugares_vendidos = []

salas_usuario = int(input("Digite quantas tem disponivel: "))
for s in range(0,salas_usuario):
    vagas_nas_salas = int(input("Digite quantas vagas: "))
    lugares_vagos.append(vagas_nas_salas)
    lugares_vendidos.append(0)

while True:
    sala = int(input("Sala (0 sai): "))
    if sala == 0:
        print("Fim")
        break
    if sala > len(lugares_vagos) or sala < 1:
        print("Sala invalida")
    elif lugares_vagos[sala - 1] == 0:
        print("Desculpe, sala lotada")
    else:
        lugares = int(input(f"Quntos lugares vc deseja {lugares_vagos[sala - 1]}: "))
        if lugares > lugares_vagos[sala - 1]:
            print("essa quantidade de lugares não esta disponivel")
        elif lugares < 0:
            print("Numero invalido")
        else:
            lugares_vagos[sala - 1]-= lugares
            lugares_vendidos[sala - 1]+= lugares
            print(f"{lugares} lugares vendidos")
    print("utilização das salas") 

    for sala, vagos in enumerate(lugares_vagos):
        print(f"Sala {sala + 1} -  {vagos} lugar(es) vazios ")   

    print()

    for sala, lv in enumerate(lugares_vendidos):
        print(f"Sala {sala + 1} ingressos vendidos {lugares_vendidos[sala]}")               