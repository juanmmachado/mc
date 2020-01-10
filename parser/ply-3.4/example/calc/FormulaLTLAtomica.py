from FormulaLTL import FormulaLTL

class FormulaLTLAtomica(FormulaLTL):
	"Formula LTL atomica"
	def __init__(self, nombre):
		self.__nombre = nombre
	
	def getAtomicas(self):
		return [self.__nombre]

	def getSubFormulas(self):
		return [self]
	
	def isTrue(self):
		return (self.__nombre == "TRUE")
	
	def getSubFormulasPositivas(self):
		return [self]

	def compararFormula(self, f):
		if isinstance(f, FormulaLTLAtomica):
			return (self.__nombre == f.__nombre)
		else:
			return False

	def verificaAtomica(self, nombre):
		return (self.__nombre == nombre) or (nombre == "TRUE")

	def imprimirFormula(self):
		return self.__nombre
		