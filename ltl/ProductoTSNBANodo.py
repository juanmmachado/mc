from FormulaLTL import FormulaLTL
from ProductoTSNBATransicion import ProductoTSNBATransicion

class ProductoTSNBANodo(object):
	"Nodo de Automata de Buchi"
	def __init__(self, nodots, nodonba):
		self.__id = -1
		self.__nodoTS = nodots
		self.__nodoNBA = nodonba
		self.__transiciones = []

	def getId(self):
		return self.__id
	
	def setId(self, id):
		self.__id = id
	
	def getNodoTS(self):
		return self.__nodoTS
		
	def getNodoNBA(self):
		return self.__nodoNBA
		
	def getTransiciones(self):
		return self.__transiciones

	def agregarTransicion(self, accion, ady):
#		if ady not in self.__adyacentes:
		self.__transiciones.append(ProductoTSNBATransicion(accion, ady))

	def imprimirTraza(self):
		print self.__nodoTS.getProposiciones()
