def numero_palindromo():
    numero = input("Digite: ")
    numero_reverso = ""

    for i in numero[::-1]:
        numero_reverso+= i
    if numero_reverso == numero:
        print(f"Numero é palindromo {int(numero)} | {int(numero_reverso)}")   
    else:
        print(f"Numero não é palindromo {int(numero)} | {int(numero_reverso)}")    


numero_palindromo()