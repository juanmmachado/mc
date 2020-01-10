from TSEstado import TSEstado

class TS(object):
	"Sistema de transiciones"
	def __init__(self, estados, iniciales):
		self.__idParaAgregar = ""
		self.__nombreParaAgregar = ""
		self.__estados = []
		self.__iniciales = []
		# genero estados
		idEstado = 0
		for estado in estados:
			nuevo = TSEstado(estado, idEstado)
			idEstado += 1
			self.__estados.append(nuevo)
			if estado in iniciales:
				self.__iniciales.append(nuevo)
	
	def agregarTransicion(self, origen, destino):
		estOrigen = self.buscarEstado(origen)
		estDestino = self.buscarEstado(destino)
		estOrigen.agregarAdyacente(estDestino)
	
	def agregarTransicionId(self, origen, destino):
		estOrigen = self.buscarEstadoId(origen)
		estDestino = self.buscarEstadoId(destino)
		estOrigen.agregarAdyacente(estDestino)
	
	def getIniciales(self):
		return self.__iniciales
	
	def buscarEstado(self, nombre):
		for estado in self.__estados:
			if (estado.getNombre() == nombre):
				return estado
		return None

	def buscarEstadoId(self, id):
		for estado in self.__estados:
			if (estado.getId() == id):
				return estado
		return None
		
	def preAgregarEstadoId(self, id):
		self.__idParaAgregar = id
		
	def preAgregarEstadoNombre(self, nombre):
		self.__nombreParaAgregar = nombre
	
	def agregarEstado(self, id, nombre):
		nuevo = TSEstado(nombre, id)
		self.__estados.append(nuevo)
		# self.__nombreParaAgregar = ""
		# self.__idParaAgregar = ""

	def agregarEstadoInicial(self, id, nombre):
		nuevo = TSEstado(nombre, id)
		self.__estados.append(nuevo)
		self.__iniciales.append(nuevo)
		# self.__nombreParaAgregar = ""
		# self.__idParaAgregar = ""

	def normalizarEstados(self, atomicas):
		for estado in self.__estados:
			if estado.getNombre() not in atomicas:
				estado.setTRUE()
	
	def imprimirTS(self):
		print "iniciales:"
		for estado in self.__iniciales:
			print "("
			estado.imprimirTSEstado()
			print ")"
		print "estados:"
		i = 100
		for estado in self.__estados:
			print i
			print "("
			estado.imprimirTSEstado()
			print ")"
			i += 1
			print "adyacentes:"
			for ady in estado.getEstadosAdyacentes():
				print "("
				ady.imprimirTSEstado()
				print ")"
				