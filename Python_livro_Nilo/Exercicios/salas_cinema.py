lista = [10, 2, 1, 3, 0]
lista_qtd_ingressos_sala = [0,0,0,0,0]

soma = 0

while True:
    sala = int(input("Digite uma sala, 0 para sair: "))
    print(lista[sala -1])

    if sala == 0:
        print("\nSalas e quantidade de lugares disponíveis:")
        salas_disponiveis = 0

        for sala_atual, vagas in enumerate(lista, start=1):
            if vagas > 0:
                salas_disponiveis += 1
                print(f"Sala {sala_atual}: {vagas} lugares disponíveis")
            else:
                print(f"Sala {sala_atual}: lotada")

        print(f"Total de salas disponíveis: {salas_disponiveis}")
        print("saindo...")
        break
    if sala > len(lista) or sala < 1:
        print("sala invalida")
    elif lista[sala -1] == 0:
        print("nao tem vagas")  
    else:
        preencher = int(input(f"Quantos lugares restantes {lista[sala -1]} "))
        if preencher > lista[sala -1]:
            print("Sem vagas disponiveis")
        elif preencher < 0:
            print("Digite um numero valido")
        else:
            lista[sala -1]-= preencher
            lista_qtd_ingressos_sala[sala - 1] = preencher
            print(f"Lugares vendidos {preencher}")

for sala, vaga in enumerate(lista):
    print(f"sala: {sala + 1} | vaga: {vaga}")                    

for i in lista_qtd_ingressos_sala:
    soma+= i

print("Total: ",soma)    