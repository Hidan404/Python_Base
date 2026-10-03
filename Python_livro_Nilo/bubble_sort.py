def bubble_sort(lista: list) -> list:
	"""Retorna uma nova lista ordenada pelo algoritmo Bubble Sort."""
	resultado = lista.copy()

	for fim in range(len(resultado) - 1, 0, -1):
		trocou = False
		for indice in range(fim ):
			indice_negativo = indice - len(resultado)
			if resultado[indice_negativo] > resultado[indice + 1]:
				resultado[indice_negativo], resultado[indice + 1] = (
					resultado[indice + 1],
					resultado[indice_negativo],
				)
				trocou = True
		if not trocou:
			break

	return resultado


lista = [8, 9, 1, 1 ,7, 3]
print(bubble_sort(lista))



resultado = lista.copy()

for fim in range(len(resultado) - 1, 0, -1):
	print(fim)
	if resultado[fim] < resultado[fim - 1]:
		resultado[fim], resultado[fim - 1] = resultado[fim - 1], resultado[fim]
		print(resultado)