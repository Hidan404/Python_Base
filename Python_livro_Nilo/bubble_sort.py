from functools import reduce


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


# Os exemplos abaixo usam a mesma lista para demonstrar as três funções.
numeros = [1, 2, 3, 4, 5]

# map(funcao, iteravel) aplica a função a cada elemento. O resultado é um
# iterador; list() é usado aqui para exibir todos os valores.
dobrados = list(map(lambda numero: numero * 2, numeros))
print("map - dobra cada número:", dobrados)  # [2, 4, 6, 8, 10]

# filter(teste, iteravel) mantém somente os elementos cujo teste retorna True.
pares = list(filter(lambda numero: numero % 2 == 0, numeros))
print("filter - mantém os pares:", pares)  # [2, 4]

# reduce(funcao, iteravel, valor_inicial) combina os itens em um único valor.
# A cada passo, soma o acumulado ao próximo número; 0 inicia o acumulador.
soma = reduce(lambda acumulado, numero: acumulado + numero, numeros, 0)
print("reduce - soma os números:", soma)  # 15

