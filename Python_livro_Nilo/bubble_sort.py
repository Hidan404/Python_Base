def bubble_sort(lista: list) -> list:
	"""Retorna uma nova lista ordenada pelo algoritmo Bubble Sort."""
	resultado = lista.copy()

	for fim in range(len(resultado) - 1, 0, -1):
		trocou = False
		for indice in range(fim):
			if resultado[indice] > resultado[indice + 1]:
				resultado[indice], resultado[indice + 1] = (
					resultado[indice + 1],
					resultado[indice],
				)
				trocou = True
		if not trocou:
			break

	return resultado


lista = [8, 9, 1, 7, 3]
bubble_sort(lista)

