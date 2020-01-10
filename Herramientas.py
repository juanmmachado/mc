class Herramientas(object):
	def __init__(self):
		pass

	def combinarListas(self, lista1, lista2):
		listaCombinada = lista1[:]
		for item in lista2:
			if item not in lista1:
				listaCombinada.append(item)
		return listaCombinada

	def interseccionListas(self, lista1, lista2):
		listaInterseccion = []
		for item in lista1:
			if item in lista2:
				listaInterseccion.append(item)
		return listaInterseccion

	def restarListas(self, lista1, lista2):
		listaResta = lista1[:]
		for item in lista2:
			listaResta.remove(item)
		return listaResta