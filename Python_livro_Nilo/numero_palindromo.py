def verificar_palindromo(numero):
    numero = str(numero)
    numero_invertido = numero[::-1]
    if numero_invertido == numero:
        print(f"Numero e palidromo {numero} == {numero_invertido}")

#verificar_palindromo(454)    

def verificar_palindromo2(n):
    numero = ''.join(reversed(str(n).split()))
    print(numero)
    n = str(n)
    if numero == n:
        print(f"Numero e palidromo {numero} == {n}")

verificar_palindromo2(454)
