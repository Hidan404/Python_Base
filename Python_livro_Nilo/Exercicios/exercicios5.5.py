def muyltiplos_de_tres():
    contador = 0
    for i in range(1,100):
        if i % 3 == 0:
            contador+= 1
            print(f"{contador} = {i}")
            
            if contador == 10:
                break


muyltiplos_de_tres()
