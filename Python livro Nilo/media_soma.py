lista = [2,85,6,8,10,6]

def soma(list):
    total = 0
    for ns in list:
        total+= ns
    return total

def media(m):
    soma_geral = soma(lista) / len(lista) 
    return soma_geral


print(media(10))    
