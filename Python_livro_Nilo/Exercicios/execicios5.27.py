def numero_palindromo():
    numero = input("Digite: ")
    numero_reverso = ""

    for i in numero[::-1]:
        numero_reverso+= i
    if numero_reverso == numero:
        print(f"Numero é palindromo {int(numero)} | {int(numero_reverso)}")   
    else:
        print(f"Numero não é palindromo {int(numero)} | {int(numero_reverso)}")    

def numero_reverso2():
    numero = input("Digite: ")
    invertido = "".join(reversed(numero))
    if invertido == numero:
        print(f"Numero é palindromo {int(numero)} | {int(invertido)}") 
    else:
        print(f"Numero não é palindromo {int(numero)} | {int(invertido):>15}")    


#numero_palindromo()
numero_reverso2()