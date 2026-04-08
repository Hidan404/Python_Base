import random

def quick_sort(lista):
    # Caso base: se a lista tem 0 ou 1 item, ela já está ordenada
    if len(lista) <= 1:
        return lista
    
    # Escolha do pivô (elemento central)
    pivo = lista[len(lista) // 2]
    
    # Listas auxiliares (substituindo as comprehensions)
    esquerda = []
    meio = []
    direita = []
    
    # Separando os elementos manualmente
    for x in lista:
        if x < pivo:
            esquerda.append(x)
        elif x == pivo:
            meio.append(x)
        else:
            direita.append(x)
    
    # Chamada recursiva e junção dos resultados
    return quick_sort(esquerda) + meio + quick_sort(direita)


numeros = [random.randint(1, 100) for _ in range(10)]

print(quick_sort(numeros)) # Saída: [11, 12, 22, 25, 34, 64, 90]
