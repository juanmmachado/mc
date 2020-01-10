from FormulaCTL import FormulaCTL

class FormulaCTLUnaria(FormulaCTL):
	"Formula LTL con conectivo unario"
	def __init__(self, sf):
		self.__subFormula = sf
		self.__sat = None

	def normalizar(self):
		self.__subFormula = self.__subFormula.normalizar()
		return self
	
	def getAtomicas(self):
		"Devuelve el conjunto de formulas atomicas"
		return self.__subFormula.getAtomicas()

	def getSubFormula(self):
		"Devuelve la subformula"
		return self.__subFormula

	def isTrue(self):
		return False

	def getSubFormulas(self):
		"Devuelve el conjunto de todas las subformulas"
		sfs = self.__subFormula.getSubFormulas()
		sfs.append(self)
		return sfs
	
	def getSubFormulasPositivas(self):
		"Devuelve el conjunto de todas las subformulas positivas"
		sfs = self.__subFormula.getSubFormulasPositivas()
		sfs.append(self)
		return sfs

	def verificaAtomica(self, nombre):
		"Compara la formula con la proposicion nombre"
		return (nombre == "TRUE")

	def getAtrSat(self):
		"Devuelve los estados de ts que la satisfacen (guardados previamente)"
		return self.__sat[:]
	
	def setAtrSat(self, sat):
		"Guarda los estados de ts que la satisfacen"
		self.__sat = sat
