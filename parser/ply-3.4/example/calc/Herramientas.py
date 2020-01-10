class Herramientas(object):
	def __init__(self):
		pass

	def combinarListas(self, lista1, lista2):
		listaCombinada = lista1[:]
		for item in lista2:
			if item not in lista1:
				listaCombinada.append(item)
		return listaCombinada
