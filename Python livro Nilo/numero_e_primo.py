def numero_e_primo(numero):
    if numero < 2:
        return False
    
    for i in range(2, int(numero ** 0.5)+ 1):
        if numero % i == 0:
            return False
    return True    

numero = int(input("Digite o numero: "))       
for i in range(0, numero):
    if numero_e_primo(i):
        print(f"Numero e primo: {i}")    
    else:
        print(f"Numero não e primo: {i}")             