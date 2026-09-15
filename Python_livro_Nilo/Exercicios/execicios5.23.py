

def eh_primo():
    numero = [n for n in range(1,101)]
    numero_parada = int(input("Digite: "))
     
    for i in numero:
        
        if i < 2:
            continue
        if i > numero_parada:
            break
            
        primo = True

        for divisor in range(2, i):
            if i % divisor == 0:
                primo = False
                break
        if primo:
            print(f"Numero: {i} é primo")
        else:
            print(f"Numero: {i} não é primo")

          

            

             

                

          


eh_primo()       