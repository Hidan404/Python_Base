def pesquisa_lista(lista, valor):
    for i, v in enumerate(lista):
        if v == valor:
            return f"Valor encontrado no índice {i}"
    return -1

print(pesquisa_lista([1, 2, 3, 4, 5], 3))  # Saída: 2
print(pesquisa_lista(['a', 'b', 'c'], 'd'))  #