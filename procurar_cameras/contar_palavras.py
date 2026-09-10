palavras = ["foi", "foi", "quando", "igual"]

def contar():
    palvars_dict = {}
    for p in palavras:
        if palvars_dict.get(p):
            palvars_dict[p] += 1
        else:
            palvars_dict[p] = 1
    return palvars_dict

numeros = [1,2,3,4,5,6,7,8,9,10]

def numeros_pares(numeros):
    for n in numeros:
        if n % 2 == 0:
            print(f"Numero é par: {n}")

def eh_primo(numero):
    if numero < 2:
        return False

    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            return True
    return False    

def lista_primos(numero_maximo):
    lista = []

    for i in range(2, numero_maximo + 1):
        if eh_primo(i):
            lista.append(i)

    return lista        
numeros_pares(numeros)            

print(contar())


limite = 100

lista_primos_numeros = lista_primos(limite)
print(lista_primos_numeros)


def fatorial(n):
    if n <= 0 or n == 1:
        return 1
    return n * fatorial(n -1)

def lista_fatorias(limite):
    lista = []

    for i in range(2, limite + 1):
        lista.append(fatorial(i))

    return lista

lista_fatorial = lista_fatorias(limite)
print(lista_fatorial)
    