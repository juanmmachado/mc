from FormulaLTL import FormulaLTL

class NodoNBA(Nodo):
	"Nodo de Automata de Buchi"
	def __init__(self, nodo, numero):
		Nodo.__init__(self, nodo.getFormulas(), nodo.getId())
		self.__numero = numero
	
	def getNumero():
		return self.__numero
