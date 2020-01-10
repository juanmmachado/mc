from FormulaLTL import FormulaLTL

class Nodo(object):
	"Nodo de Automata de Buchi"
	def __init__(self, formulas, id):
		self.__id = id											#corregir
		self.__formulas = formulas
		self.__adyacentes = []
	
	def getId(self):
		return self.__id
	
	def getFormulas(self):
		return self.__formulas
		
	def getAdyacentes(self):
		adys = []
		for nodo in self.__adyacentes:
			adys.append(nodo.getId())
		return adys
	
	def getEstadosAdyacentes(self, nombre):
		adys = []
		for nodo in self.__adyacentes:
			if nodo.verificaAtomica(nombre):					# CAMBIE if self.verificaAtomica(nombre):
				adys.append(nodo)
		return adys

	def getNodosAdyacentes(self):
		return self.__adyacentes
	
	def perteneceFormula(self, formula):
		return formula.perteneceLista(self.__formulas)
	
	def agregarAdyacente(self, ady):
		self.__adyacentes.append(ady)

	def verificaAtomica(self, nombre):
		for formula in self.__formulas:
			if formula.verificaAtomica(nombre):
				return True
		return False

	def imprimirEstado(self):
		print "estado:", self.__id
		for f in self.__formulas:
			print f.imprimirFormula()
			