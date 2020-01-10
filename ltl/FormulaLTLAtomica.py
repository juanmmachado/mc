from FormulaLTL import FormulaLTL

class FormulaLTLAtomica(FormulaLTL):
	"Formula LTL atomica"
	def __init__(self, nombre):
		self.__nombre = nombre

	def normalizar(self):
		return self
		
	def obtenerNombreAtomica(self):
		"Devuelve el nombre de la formula"
		return self.__nombre
	
	def obtenerNombreNegacionAtomica(self):
		"Al no ser una negacion de atomica devuelve el string vacio."
		return ""
	
	def getAtomicas(self):
		"Devuelve el conjunto de todas las subformulas atomicas (se devuelve a si misma)."
		return [self.__nombre]

	def getSubFormulas(self):
		"Devuelve el conjunto de todas las subformulas."
		return [self]
	
	def getSubFormulasPositivas(self):
		"Devuelve el conjunto de todas las subformulas cuyo conectivo principal no es una negacion."
		return [self]

	def compararFormula(self, f):
		"Devuelve True si la formula es igual a f."
		if isinstance(f, FormulaLTLAtomica):
			return (self.__nombre == f.__nombre)
		else:
			return False

	def verificaAtomica(self, nombre):
		return (self.__nombre == nombre) or (nombre == "TRUE")

	def imprimirFormula(self):
		return self.__nombre

	def verificarTrazaV(self, traza):
		if traza == []:
			return traza
		if not traza[0].getNodoTS().satAtomica(self.__nombre):
			return traza
		return [traza[0]]

	def verificarTrazaF(self, traza):
		if traza == []:
			return traza
		if traza[0].getNodoTS().satAtomica(self.__nombre):
			return traza
		return [traza[0]]
	
	def verificarTrazaVTrans(self, traza):
		if traza == []:
			return traza
		if not traza[0].getDestino().getNodoTS().satAtomica(self.__nombre):
			return traza
		return [traza[0]]

	def verificarTrazaFTrans(self, traza):
		if traza == []:
			return traza
		if traza[0].getDestino().getNodoTS().satAtomica(self.__nombre):
			return traza
		return [traza[0]]
