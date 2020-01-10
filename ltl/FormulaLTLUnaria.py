from FormulaLTL import FormulaLTL

class FormulaLTLUnaria(FormulaLTL):
	"Formula LTL con conectivo unario"
	def __init__(self, sf):
		self.__subFormula = sf

	def obtenerNombreAtomica(self):
		"Al no ser una formula atomica devuelve el string vacio."
		return ""
	
	def getAtomicas(self):
		"Devuelve el conjunto de todas las subformulas atomicas."
		return self.__subFormula.getAtomicas()

	def getSubFormula(self):
		"Devuelve la subformula."
		return self.__subFormula

	def isTrue(self):
		return False

	def normalizar(self):
		self.__subFormula = self.__subFormula.normalizar()
		return self
	
	def getSubFormulas(self):
		"Devuelve el conjunto de todas las subformulas."
		sfs = self.__subFormula.getSubFormulas()
		sfs.append(self)
		return sfs
	
	def getSubFormulasPositivas(self):
		"Devuelve el conjunto de todas las subformulas cuyo conectivo principal no es una negacion."
		sfs = self.__subFormula.getSubFormulasPositivas()
		sfs.append(self)
		return sfs

	def verificaAtomica(self, nombre):
		return (nombre == "TRUE")
