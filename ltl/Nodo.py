from FormulaLTL import FormulaLTL

class Nodo(object):
	"Nodo de Automata de Buchi"
	def __init__(self, formulas, id):
		# identificador del nodo
		self.__id = id
		# conjunto de proposiciones validas en el nodo
		self.__formulas = formulas
		# conjunto de nodos adyacentes
		self.__adyacentes = []
	
	def getId(self):
		return self.__id
	
	def getFormulas(self):
		return self.__formulas
	
	def getFormulasString(self):
		if self.__formulas == []:
			return ""
		sform = self.__formulas[0].imprimirFormula()
		for i in range(1, len(self.__formulas)):
			sform = sform + "," + self.__formulas[i].imprimirFormula()
		return sform
	
	def isTrue(self):
		for formula in self.__formulas:
			if formula.isTrue():
				return True
		return False
	
	def getAdyacentes(self):
		"Devuelve los identificadores de los nodos adyacentes."
		adys = []
		for nodo in self.__adyacentes:
			adys.append(nodo.getId())
		return adys
	
	def getEstadosAdyacentes(self, props):
		"Devuelve los nodos adyacentes en los cuales valen las proposiciones dadas."
		adys = []
		for nodo in self.__adyacentes:
			if nodo.verificaAtomicas(props):
				adys.append(nodo)
		return adys

	def getNodosAdyacentes(self):
		"Devuelve el conjunto de los nodos adyacentes."
		return self.__adyacentes
	
	def perteneceFormula(self, formula):
		"Devuelve True si la formula pertenece al nodo."
		return formula.perteneceLista(self.__formulas)
	
	def agregarAdyacente(self, ady):
		"Agrega un nodo adyacente."
		self.__adyacentes.append(ady)

	def verificaAtomicas(self, props):
		"Devuelve True si el nodo verifica las proposiciones."
		negaciones = FormulaLTL().obtenerNombresNegacionesAtomicas(self.__formulas)
		atomicas = FormulaLTL().obtenerNombresAtomicas(self.__formulas)
		if "TRUE" in atomicas:
			atomicas.remove("TRUE")
		# ningun nodo verifica Not True
		if "TRUE" in negaciones:
			return False
		for at in atomicas:
			if at not in props:
				return False
		for negn in negaciones:
			if negn in props:
				return False
		return True
	
	def verificaAtomica(self, nombre):
		"Devuelve True si el nodo verifica la proposicion nombre"
		for formula in self.__formulas:
			if formula.verificaAtomica(nombre):
				return True
		return False
