class TSEstado(object):
	"Estado de sistema de transiciones"
	def __init__(self, nombre, id):
		self.__id = id
		self.__nombre = nombre
		self.__adyacentes = []
	
	def getId(self):
		return self.__id
	
	def getNombre(self):
		return self.__nombre
	
	def setTRUE(self):
		self.__nombre = "TRUE"
	
	def getEstadosAdyacentes(self):
		return self.__adyacentes
	
	def agregarAdyacente(self, ady):
		self.__adyacentes.append(ady)

	def imprimirTSEstado(self):
		print self.__id
		print self.__nombre