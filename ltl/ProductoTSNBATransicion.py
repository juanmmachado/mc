class ProductoTSNBATransicion(object):
	"Transicion de Automata de Buchi"
	def __init__(self, accion, destino):
		self.__accion = accion
		self.__destino = destino

	def getAccion(self):
		"Devuelve la accion correspondiente a la transicion."
		return self.__accion

	def getDestino(self):
		"Devuelve el estado de destino de la transicion."
		return self.__destino

	def imprimirTraza(self):
		print "-- ", self.__accion, " -->"
		self.__destino.imprimirTraza()
		