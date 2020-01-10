from FormulaLTL import FormulaLTL

class NodoProductoTSNBA(object):
	"Nodo de Automata de Buchi"
	def __init__(self, nodots, nodonba):
		self.__nodoTS = nodots
		self.__nodoNBA = nodonba
		self.__adyacentes = []

	def getNodoTS(self):
		return self.__nodoTS
		
	def getNodoNBA(self):
		return self.__nodoNBA
		
	def getAdyacentes(self):
		return self.__adyacentes

	def agregarAdyacente(self, ady):
		if ady not in self.__adyacentes:
			self.__adyacentes.append(ady)
