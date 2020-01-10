from TSTransicion import TSTransicion

class TSEstado(object):
	"Estado de sistema de transiciones"
	def __init__(self, proposiciones, id):
		self.__id = id
		self.__proposiciones = proposiciones
		self.__transiciones = []
	
	def getId(self):
		"Devuelve el Id"
		return self.__id
	
	def setId(self, id):
		"Asigna el Id"
		self.__id = id
	
	def getProposiciones(self):
		"Devuelve el conjunto de proposiciones del estado."
		return self.__proposiciones
	
	def getTransiciones(self):
		"Devuelve el conjunto de transiciones desde el estado."
		return self.__transiciones
	
	def getTransicionesAccion(self, accion):
		"Devuelve el conjunto de transiciones con la accion dada."
		t_accion = []
		for t in self.__transiciones:
			if (t.getAccion() == accion):
				t_accion.append(t)
		return t_accion
	
	def setTRUE(self):
		self.__proposiciones = ["TRUE"]
	
	def getEstadosAdyacentes(self):
		"Devuelve los estados adyacentes (posteriores)"
		adyacentes = []
		for t in self.__transiciones:
			adyacentes.append(t.getDestino())
		return adyacentes
	
	def agregarAdyacente(self, accion, ady):
		"Agrega un estado adyacente (posterior)"
		self.__transiciones.append(TSTransicion(accion, ady))

	def satAtomica(self, at):
		"Devuelve True si satisface la formula at"
		if at in self.__proposiciones:
			return True
		return False

	def imprimirTraza(self):
		print self.__proposiciones
