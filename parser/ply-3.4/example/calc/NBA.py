from FormulaLTL import FormulaLTL
from Nodo import Nodo

class NBA(object):
	"Automata de Buchi"
	def __init__(self, gnba):
		self.__estados = []
		self.__iniciales = []
		self.__acceptanceSet = []

	def agregarEstados(self, estados):
		self.__estados.extend(estados)
	
	def getEstadosI(self, n):
		estados_n = []
		for nodo in self.__estados:
			if (nodo.getNumero() == n):														#agregar
				estados_n.append(nodo)
		return estados_n
	
	def buscarNodo(self, id, n):
		for nodo in self.__estados:
			if (nodo.getId() == id) and (nodo.getNumero() == n):
				return nodo
		return none
	
	def agregarTransiciones(self, gnba):
		for i in range(0, len(gnba.cantAcceptanceSets())-1):
			estados_i = self.getEstadosI(i)
			for nodo in estados_i:
				i_sig = i
				if gnba.isFinalN(nodo.getId(), i):
					i_sig = (i+1)%gnba.cantAcceptanceSets()
				adys = gnba.buscarAdyacentes(nodo.getId())
				for ady in adys:
					nodoAdy = self.buscarNodo(ady, i_sig)
					nodo.agregarAdyacente(nodoAdy)

	def setIniciales(self, gnba):
		estados0 = self.getEstadosI(0)
		for nodo in estados0:
			if gnba.isInicial(nodo.getId()):
				self.__iniciales.append(nodo)
	
	def setFinales(self, gnba):
		estados0 = self.getEstadosI(0)
		for nodo in estados0:
			if gnba.isFinalN(nodo.getId(), 0):
				self.__acceptanceSet.append(nodo)
	
