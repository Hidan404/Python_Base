def numero_e_primo(numero):
    if numero < 2:
        return False
    
    for i in range(2, int(numero ** 0.5)+ 1):
        if numero % i == 0:
            return False
    return True    

numero = int(input("Digite o numero: "))        
if numero_e_primo(numero):
    print(f"Numero e primo: {numero}")    
else:
    print(f"Numero não e primo: {numero}")             